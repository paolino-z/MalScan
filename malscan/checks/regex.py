from malscan.engine import Check

class RegexCheck(Check):
    def __init__(self):
        self.patterns = {
            rb"powershell(\.exe)?": "PowerShell Execution Reference",
            rb"cmd\.exe": "Command Prompt Reference",
            rb"eval\(|exec\(": "Dynamic Code Execution Pattern",
            rb"system\s*\(": "System Call Pattern",
            rb"WScript\.Shell": "Windows Script Host Reference",
            rb"http[s]?://": "Network Activity Indicator"
            #da aggiungere altro
        }

    def analyze(self, file_path: str) -> dict:
        pass