from abc import ABC, abstractmethod


class FileModel(ABC):
    @abstractmethod
    def __init__(self, filename: str, content: bytes):
        pass

    @abstractmethod
    def extract_text(self) -> str:
        pass

    @abstractmethod
    def get_extension(self) -> str:
        pass