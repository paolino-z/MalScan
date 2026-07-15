import os

from .base import Check

class ExtensionCheck(Check):
    def __init__(self):
        self.sus_extensions = {
            ".exe", ".dll", ".bat", ".cmd", ".vbs", 
            ".scr", ".ps1", ".sh", ".msi", ".jar", ".pif"
        }
    
    def analyze(self, file_path):
        _, ext = os.path.splitext(file_path)
        is_sus = ext in self.sus_extensions
        return {
            "name": "Extension Security Check",
            "score": 40 if is_sus else 0,
            "details": {
                "extension": ext if ext else "None",
                "is_sus": is_sus
            }
        }