from typing import List, Optional
from .storageStrategy import StorageStrategy  
from ..models.usuario import Usuario

class ListStorageStrategy(StorageStrategy):
    def __init__(self):
        self._storage: List[Usuario] = []

    def save(self, item: Usuario) -> None:
        self._storage.append(item)

    def load(self, item_id: int) -> Optional[Usuario]:
        for item in self._storage:
            if item.id == item_id:
                return item
        return None

    def load_all(self) -> List[Usuario]:
        return self._storage

    def delete(self, item_id: int) -> bool:
        for item in self._storage:
            if item.id == item_id:
                self._storage.remove(item)
                return True
        return False

    def update(self, item_id: int, item: Usuario) -> Optional[Usuario]:
        for idx, existing_item in enumerate(self._storage):
            if existing_item.id == item_id:
                self._storage[idx] = item
                return item
        return None
