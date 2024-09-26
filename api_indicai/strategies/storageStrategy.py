from abc import ABC, abstractmethod
from typing import List, Optional
from models.usuario import Usuario

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, item: Usuario) -> None:
        pass

    @abstractmethod
    def load(self, item_id: int) -> Optional[Usuario]:
        pass

    @abstractmethod
    def load_all(self) -> List[Usuario]:
        pass

    @abstractmethod
    def delete(self, item_id: int) -> bool:
        pass

    @abstractmethod
    def update(self, item_id: int, item: Usuario) -> Optional[Usuario]:
        pass