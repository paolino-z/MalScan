import abc

class Check(abc.ABC):
    @abc.abstractmethod
    def analyze(self, file_path: str) -> dict:
        pass