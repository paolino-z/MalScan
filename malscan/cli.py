import argparse
import sys
import json
from .engine import MalScanEngine
from .checks.extension import ExtensionCheck
from .checks.regex import RegexCheck
from .checks.entropy import EntropyCheck
from .checks.hash import HashCheck
from .checks.virustotal import VirusTotalCheck

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
    parser.add_argument("--json-out", help="Percorso file di output JSON opzionale", default=None)
    parser.add_argument("--virustotal-api-key", help="API key di VirusTotal", default=None)
    args = parser.parse_args()

    engine = MalScanEngine()
    engine.add_check(HashCheck())
    engine.add_check(ExtensionCheck())
    engine.add_check(EntropyCheck())
    engine.add_check(RegexCheck())
    engine.add_check(VirusTotalCheck(api_key=args.virustotal_api_key, enabled=bool(args.virustotal_api_key)))

    try:
        report = engine.run(args.file)
        print_text_report(report)
        
        if args.json_out:
            with open(args.json_out, "w", encoding="utf-8") as jf:
                json.dump(report, jf, indent=4, ensure_ascii=False)
            print(f"\n[i] Report JSON esportato correttamente in: {args.json_out}")
            
    except Exception as e:
        print(f"[-] Errore durante l'esecuzione dell'analisi: {e}", file=sys.stderr)
        sys.exit(1)
