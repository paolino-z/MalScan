import abc

class Check(abc.ABC):
    @abc.abstractmethod
    def analyze(self, file_path: str) -> dict:
        pass

class hashcheck(Check):
    pass

class ExtensionCheck(Check):
    pass

class EntropyCheck(Check):
    pass


class RegexCheck(Check):
    pass


"""class VirusTotalCheck(Check):
    pass"""

if __name__ == "__main__":
    pass