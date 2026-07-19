import hashlib
import os
import time
import requests

from .base import Check


class VirusTotalCheck(Check):
    def __init__(self, api_key: str = None, enabled: bool = True, poll_attempts: int = 6, poll_delay: int = 10):
        self.api_key = api_key
        self.enabled = enabled
        self.poll_attempts = poll_attempts
        self.poll_delay = poll_delay

    def _fetch_file_report(self, sha256_digest: str) -> dict:
        url = f"https://www.virustotal.com/api/v3/files/{sha256_digest}"
        headers = {"x-apikey": self.api_key}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return {"status": f"API Error: Status Code {response.status_code}"}

        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        malicious_count = stats.get("malicious", 0)
        score = 100 if malicious_count > 3 else (malicious_count * 25)
        return {
            "status": "Success",
            "malicious_detections": malicious_count,
            "stats": stats,
            "score": min(score, 100)
        }

    def _poll_for_report(self, sha256_digest: str) -> dict:
        last_result = {"status": "Analisi ancora in corso"}

        for _ in range(self.poll_attempts):
            try:
                result = self._fetch_file_report(sha256_digest)
                if result.get("status") == "Success":
                    return result
                if "Status Code 404" not in result.get("status", ""):
                    return result
                last_result = result
            except Exception as e:
                last_result = {"status": f"Connection Error: {str(e)}"}
                break

            time.sleep(self.poll_delay)

        last_result["info"] = "L'analisi può richiedere più tempo; riprova più tardi su VirusTotal."
        return last_result

    def _upload_file(self, file_path: str) -> dict:
        print(f"\n[?] File non trovato su VirusTotal. Caricare l'intero file binario? (y/n): ", end="")
        scelta = input().strip().lower()
        if scelta != 'y':
            return {"status": "Upload annullato dall'utente"}

        print("[*] Caricamento del file binario in corso su VirusTotal...")
        url = "https://www.virustotal.com/api/v3/files"
        headers = {"x-apikey": self.api_key}

        try:
            with open(file_path, "rb") as f:
                files = {"file": (os.path.basename(file_path), f)}
                response = requests.post(url, headers=headers, files=files, timeout=30)

            if response.status_code in (200, 201):
                data = response.json()
                analysis_id = data["data"]["id"]
                upload_result = {
                    "status": "File caricato con successo per l'analisi",
                    "analysis_id": analysis_id,
                    "info": "L'analisi è in coda. Controllare l'ID su VirusTotal per i risultati aggiornati."
                }
                sha256_hash = hashlib.sha256()
                with open(file_path, "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)

                upload_result["analysis_result"] = self._poll_for_report(sha256_hash.hexdigest())
                return upload_result
            else:
                return {"status": f"Errore durante l'upload: Status {response.status_code}"}
        except Exception as e:
            return {"status": f"Errore di connessione durante l'upload: {str(e)}"}

    def analyze(self, file_path: str) -> dict:
        if not self.enabled:
            return {
                "name": "VirusTotal API Check",
                "score": 0,
                "details": {"status": "Skipped (VirusTotal disabled)"}
            }

        if not self.api_key:
            return {
                "name": "VirusTotal API Check",
                "score": 0,
                "details": {"status": "Skipped (No API Key provided)"}
            }

        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        try:
            report = self._fetch_file_report(sha256_hash.hexdigest())
            if report.get("status") == "Success":
                return {
                    "name": "VirusTotal API Check",
                    "score": report["score"],
                    "details": {
                        "status": report["status"],
                        "malicious_detections": report["malicious_detections"],
                        "stats": report["stats"]
                    }
                }
            if "Status Code 404" in report.get("status", ""):
                upload_result = self._upload_file(file_path)
                analysis_result = upload_result.get("analysis_result", {})
                analysis_score = analysis_result.get("score", 0) if analysis_result.get("status") == "Success" else 0
                return {
                    "name": "VirusTotal API Check",
                    "score": analysis_score,
                    "details": upload_result
                }
            return {
                "name": "VirusTotal API Check",
                "score": 0,
                "details": report
            }
        except Exception as e:
            return {
                "name": "VirusTotal API Check",
                "score": 0,
                "details": {"status": f"Connection Error: {str(e)}"}
            }
