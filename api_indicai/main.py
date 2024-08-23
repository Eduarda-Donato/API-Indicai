from models.condomino import Condomino
from models.prestador import Prestador
from enums.servico import Servico
from services.usuarioManager import UsuarioManager
from controller.usuarioController import UsuarioController

def main():
    usuario_manager = UsuarioManager()
    usuario_controller = UsuarioController(manager=usuario_manager)

    # Criação de usuários de exemplo
    condomino1 = Condomino(id=1, nome="Ana", cpf="12345678900", telefone="999999999", login="ana_login", senha=1234, bloco="A", ap="101")
    prestador1 = Prestador(id=2, nome="Carlos", cpf="09876543211", telefone="888888888", tipoServico=Servico.ELETRICISTA)

    # Adiciona usuários
    usuario_controller.create_usuario(condomino1)
    usuario_controller.create_usuario(prestador1)

    # Obtém usuário por ID
    usuario = usuario_controller.get_usuario_por_id(1)
    print(f'Usuário com ID 1: {usuario}')

    # Obtém usuários por tipo
    condominos = usuario_controller.get_usuario_por_tipo(Condomino)
    print(f'Condominos: {condominos}')

    prestadores = usuario_controller.get_usuario_por_tipo(Prestador)
    print(f'Prestadores: {prestadores}')

    # Atualiza um usuário
    condomino_atualizado = Condomino(id=1, nome="Ana Silva", cpf="12345678900", telefone="999999999", login="ana_login", senha=1478, bloco="B", ap="202")
    atualizado = usuario_controller.update_usuario(1, condomino_atualizado)
    print(f'Atualização bem-sucedida: {atualizado}')
    
    # Obtém o usuário atualizado
    usuario_atualizado = usuario_controller.get_usuario_por_id(1)
    print(f'Usuário atualizado com ID 1: {usuario_atualizado}')

    # Remove um usuário
    removido = usuario_controller.delete_usuario_por_id(2)
    print(f'Remoção bem-sucedida: {removido}')

    # Verifica se o usuário foi removido
    usuario_removido = usuario_controller.get_usuario_por_id(2)
    print(f'Usuário com ID 2: {usuario_removido}')

if __name__ == "__main__":
    main()
