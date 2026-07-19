import re
import os
from .base import Check

class RegexCheck(Check):
    def __init__(self):
        self.patterns = {
            rb"EICAR-STANDARD-ANTIVIRUS-TEST-FILE": ("EICAR Standard Anti-Virus Test File Signature", 100),

            #powershell
            rb"powershell(\.exe)?\s+.*-enc(odedcommand)?": ("PowerShell EncodedCommand", 25),
            rb"powershell(\.exe)?\s+.*-nop": ("PowerShell NoProfile", 20),
            rb"powershell(\.exe)?\s+.*-w\s+hidden": ("PowerShell Hidden Window", 20),
            rb"Invoke-Expression|IEX": ("PowerShell Invoke-Expression", 25),
            rb"DownloadString": ("PowerShell DownloadString", 20),
            rb"FromBase64String": ("Base64 Decoding", 20),

            #esecuzione codice
            rb"eval\s*\(": ("Dynamic Code Execution (eval)", 20),
            rb"exec\s*\(": ("Dynamic Code Execution (exec)", 20),
            rb"system\s*\(": ("System Call", 20),
            
            # Windows Script Host
            rb"WScript\.Shell": ("Windows Script Host", 20),

            # Networking
            rb"http[s]?://": ("Network Activity Indicator", 5),

            # cmd
            rb"cmd\.exe\s*/c": ("Command Prompt Execution", 15)
        }

        self.threshold = 40

    def analyze(self, file_path: str) -> dict:
        matches_found = {}
        score = 0
        with open(file_path, "rb") as f:
            content = f.read()
            
        for pattern, (description, weight) in self.patterns.items():
            matches = re.findall(pattern, content, re.IGNORECASE)
            
            if matches:
                matches_found[description] = len(matches)
                if b"EICAR" in pattern:
                    score = 100
                else:
                    score += min(weight * len(matches), weight * 2)        

        score = min(score, 100)
        ext = os.path.splitext(file_path)[1].lower()

        if (
            ext == ".txt"
            and score < self.threshold
            and "EICAR Standard Anti-Virus Test File Signature" not in matches_found
        ):
            score = 0

        return {
            "name": "Signature & Regex Check",
            "score": score,
            "details": {
                "matches": matches_found if matches_found else "Nessun match trovato",
            }
        }