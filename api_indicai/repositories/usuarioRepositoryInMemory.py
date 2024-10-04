from typing import List, Optional
from api_indicai.repositories.usuarioRepositoryInterface import UsuarioRepositoryInterface
from models.usuario import Usuario  

class UsuarioRepositoryInMemory(UsuarioRepositoryInterface):
    def __init__(self):
        self.usuarios: List[Usuario] = [] 
        self.current_id = 1 

    def adicionar(self, usuario: Usuario) -> Usuario:
        usuario.id = self.current_id  
        self.usuarios.append(usuario)  
        self.current_id += 1  
        return usuario

    def buscar_por_id(self, usuario_id: int) -> Optional[Usuario]:
        return next((usuario for usuario in self.usuarios if usuario.id == usuario_id), None)

    def listar_todos(self) -> List[Usuario]:
        return self.usuarios

    def remover(self, usuario_id: int) -> bool:
        usuario = self.buscar_por_id(usuario_id)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False

    def atualizar(self, usuario_id: int, usuario_atualizado: Usuario) -> Optional[Usuario]:
        usuario = self.buscar_por_id(usuario_id)
        if usuario:
            for key, value in usuario_atualizado.dict(exclude_unset=True).items():  
                setattr(usuario, key, value)
            return usuario
        return None
