from typing import List, Optional
from api_indicai.repositories.usuarioRepositoryInDB import UsuarioRepository
from api_indicai.repositories.usuarioRepositoryInterface import UsuarioRepositoryInterface
from models.usuario import Usuario
from utils.criptografarSenha import CriptografarSenha
from utils.validarUsuario import ValidarUsuario
from api_indicai.db.singletonSession import AppConfig
from observer.observer import Subject
from observer.userLogger import UserLogger
from memento.usuarioMemento import UsuarioMemento 

class UsuarioService(Subject):
    def __init__(self, usuario_repository: UsuarioRepositoryInterface):
        super().__init__()  # Inicializa o Subject para o Observer
        self.usuario_repository = usuario_repository

        # Registrando um logger como exemplo de observador
        self.register_observer(UserLogger())

        # Adicionando atributo para armazenar o último Memento do usuário
        self._memento = None

    def create_usuario(self, usuario: Usuario) -> Usuario:
        # Validação do usuário
        is_valid, erros = ValidarUsuario.validar(usuario)
        if not is_valid:
            raise ValueError(f"Erro(s) de validação: {', '.join(erros)}")

        # Criptografia da senha
        if usuario.tipousuario == "condomino":
            usuario.senha = CriptografarSenha.hash_senha(usuario.senha)

        usuario_db = self.usuario_repository.adicifonar(usuario)
        
        # Notifica os observadores após a criação do usuário
        self.notify_observers(f"Usuário criado: {usuario_db}")

        return usuario_db

    def get_usuarios(self) -> List[Usuario]:
        usuarios_db = self.usuario_repository.listar_todos()
        return [Usuario.model_validate(usuario_db) for usuario_db in usuarios_db]

    def get_usuario_por_id(self, usuario_id: int) -> Optional[Usuario]:
        usuario_db = self.usuario_repository.buscar_por_id(usuario_id)
        if usuario_db:
            return Usuario.model_validate(usuario_db)
        return None

    def update_usuario(self, usuario_id: int, usuario: Usuario) -> Optional[Usuario]:
        # Validação do usuário
        is_valid, erros = ValidarUsuario.validar(usuario)
        if not is_valid:
            raise ValueError(f"Erro(s) de validação: {', '.join(erros)}")

        # Cria um Memento antes de atualizar
        self._memento = self.create_memento(usuario_id)

        # Criptografa a senha se for fornecida
        if usuario.senha:
            usuario.senha = CriptografarSenha.hash_senha(usuario.senha)

        usuario_db = self.usuario_repository.atualizar(usuario_id, usuario)
        if usuario_db:
            # Notifica os observadores após a atualização do usuário
            self.notify_observers(f"Usuário atualizado: {usuario_db}")
            return Usuario.model_validate(usuario_db)
        return None

    def delete_usuario_id(self, usuario_id: int) -> bool:
        sucesso = self.usuario_repository.remover(usuario_id)
        
        # Notifica os observadores após a remoção do usuário
        if sucesso:
            self.notify_observers(f"Usuário deletado: ID {usuario_id}")

        return sucesso

    # Função para criar um Memento do estado atual do usuário
    def create_memento(self, usuario_id: int) -> UsuarioMemento:
        usuario = self.get_usuario_por_id(usuario_id)
        if usuario:
            return UsuarioMemento(usuario)
        return None

    # Função para restaurar o estado do último Memento
    def restore_memento(self) -> Optional[Usuario]:
        if self._memento:
            estado_anterior = self._memento.get_estado()
            usuario_db = self.update_usuario(estado_anterior.id, estado_anterior)

            # Notifica os observadores após restaurar o estado anterior do usuário
            if usuario_db:
                self.notify_observers(f"Usuário restaurado para o estado anterior: {usuario_db}")
                
            return usuario_db
        return None
