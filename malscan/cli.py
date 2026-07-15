import argparse
from .engine import MalScanEngine
from .checks.extension import ExtensionCheck
from .checks.regex import RegexCheck

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

    args = parser.parse_args()

    engine = MalScanEngine()
    #engine.add_check(HashCheck())
    engine.add_check(ExtensionCheck())
    #engine.add_check(EntropyCheck())
    engine.add_check(RegexCheck())
    #engine.add_check(VirusTotalCheck(api_key=""))

    report = engine.run(args.file)
    print_text_report(report)