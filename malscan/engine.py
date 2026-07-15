import os

class MalScanEngine:
    def __init__(self):
        self.checks = []

    def add_check(self, check):
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
