import hashlib

from .base import Check


class HashCheck(Check):
    def analyze(self, file_path: str) -> dict:
        md5_hash = hashlib.md5()
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha256_hash.update(byte_block)
        return {
            "name": "Hash Analysis",
            "score": 0,
            "details": {
                "md5": md5_hash.hexdigest(),
                "sha256": sha256_hash.hexdigest()
            }
        }
