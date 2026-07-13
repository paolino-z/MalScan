import abc
import argparse
import os
from checks.hash import HashCheck
from checks.extension import ExtensionCheck
from checks.entropy import EntropyCheck
from checks.regex import RegexCheck

class Check(abc.ABC):
    @abc.abstractmethod
    def analyze(self, file_path: str) -> dict:
        pass

class engine:
    def __init__(self):
        self.checks = []

    def add_check(self, check: Check):
        self.checks.append(check)

    def run(self, file_path: str) -> dict:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Il file '{file_path}' non esiste.")
        
        results = []
        for check in self.checks:
            try:
                results.append(check.analyze(file_path))
            except Exception as e:
                results.append({
                    "name": check.__class__.__name__,
                    "score": 0,
                    "details": {"error": str(e)}
                })
        
        total_score = sum(res["score"] for res in results)
        final_score = min(total_score, 100)  # punteggio massimo 100

        risk_level = "Basso"
        if final_score >= 70:
            risk_level = "Alto"
        elif final_score >= 30:
            risk_level = "Medio"

        return {
            "file": os.path.basename(file_path),
            "risk_score": final_score,
            "risk_level": risk_level,
            "reports": results
        }
    
def print_text_report(report: dict):
    print("=" * 60)
    print(f" MALSCAN REPORT : {report['file'].upper()}")
    print("=" * 60)
    print(f"Punteggio di rischio: {report['risk_score']}")
    print(f"Livello di rischio: {report['risk_level']}")
    print("-" * 60)
    
    for r in report["reports"]:
        print(f"\n[+] {r['name']}")
        print(f"    Punteggio parziale: {r['score']}")
        for k, v in r["details"].items():
            if isinstance(v, dict):
                print(f"    {k.capitalize()}:")
                for sub_k, sub_v in v.items():
                    print(f"      - {sub_k}: {sub_v}")
                else:
                    print(f"    {k.capitalize()}: {v}")
        print("=" * 60)

def main():
    parser = argparse.ArgumentParser(description="MalScan - Analizzatore di file")
    parser.add_argument("file", help="Percorso del file da analizzare")

    engine = engine()
    engine.add_check(HashCheck())
    engine.add_check(ExtensionCheck())
    engine.add_check(EntropyCheck())
    engine.add_check(RegexCheck())
    #engine.add_check(VirusTotalCheck(api_key=""))