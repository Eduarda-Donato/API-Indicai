from api_indicai.services.usuarioService import UsuarioService
from api_indicai.strategies.storage_factory import get_storage_strategy

def get_usuario_service():
    storage_strategy = get_storage_strategy()
    return UsuarioService(storage_strategy=storage_strategy)