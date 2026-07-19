import math
import os
from .base import check

class EntropyCheck(Check):
    def analyze(self, file_path: str) -> dict:
        if not os.path.exists(file_path):
            return {"name": "Entropy Analysis", "score": 0, "details": {"error": "File not found"}}
            
        with open(file_path, "rb") as f:
            data = f.read()
        if not data:
            return {"name": "Entropy Analysis", "score": 0, "details": {"entropy": 0.0, "packed_or_encrypted": False}}
        
        entropy = 0.0
        length = len(data)
        counts = [0] * 256
        for byte in data:
            counts[byte] += 1
            
        for count in counts:
            if count > 0:
                p = count / length
                entropy -= p * math.log2(p)
                
        is_packed = entropy > 7.2
        return {
            "name": "Entropy Analysis",
            "score": 35 if is_packed else 0,
            "details": {
                "entropy": round(entropy, 4),
                "packed_or_encrypted": is_packed
            }
        }
