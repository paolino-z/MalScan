import re
from .base import Check

class RegexCheck(Check):
    def __init__(self):
        self.patterns = {
            rb"EICAR-STANDARD-ANTIVIRUS-TEST-FILE": "EICAR Standard Anti-Virus Test File Signature",
            rb"powershell(\.exe)?": "PowerShell Execution Reference",
            rb"cmd\.exe": "Command Prompt Reference",
            rb"eval\(|exec\(": "Dynamic Code Execution Pattern",
            rb"system\s*\(": "System Call Pattern",
            rb"WScript\.Shell": "Windows Script Host Reference",
            rb"http[s]?://": "Network Activity Indicator"
            #da aggiungere altro
        }

    def analyze(self, file_path: str) -> dict:
        matches_found = {}
        score = 0
        with open(file_path, "rb") as f:
            content = f.read()
            
        for pattern, description in self.patterns.items():
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                matches_found[description] = len(matches)
                if b"EICAR" in pattern:
                    score += 100
                else:
                    score += min(20 * len(matches), 40)
                
        return {
            "name": "Signature & Regex Check",
            "score": min(score, 100 if "EICAR Standard Anti-Virus Test File Signature" in matches_found else 60),
            "details": {
                "matches": matches_found if matches_found else "Nessun match trovato"
            }
        }