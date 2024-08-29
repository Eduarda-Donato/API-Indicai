from controller.usuarioController import UsuarioController
from services.usuarioManager import UsuarioManager
from models.condomino import Condomino
from models.prestador import Prestador
from enums.servico import Servico

def main():
    manager = UsuarioManager()
    controller = UsuarioController(manager)
    
    condomino_valido = Condomino(
        id=1, nome="Ana", cpf="12345678900", telefone="999999999", login="ana_login", senha="Senha@123", bloco="A", ap="101"
    )
    prestador_valido = Prestador(
        id=2, nome="Carlos", cpf="09876543211", telefone="888888888", login="carlos_login", senha="Senha@456", bloco="A", ap="102", tipoServico=Servico.ELETRICISTA
    )

    condomino_invalido = Condomino(
        id=3, nome="Lucas", cpf="98765432100", telefone="777777777", login="lu", senha="123", bloco="B", ap="202"
    )
    prestador_invalido = Prestador(
        id=4, nome="Maria", cpf="12345678999", telefone="666666666", login="maria_login", senha="abc", bloco="C", ap="302", tipoServico=Servico.LIMPEZA
    )
    
    print("Criando usuários válidos...")
    if controller.create_usuario(condomino_valido):
        print("Condomino válido criado com sucesso!")
    else:
        print("Falha ao criar condomino válido.")

    if controller.create_usuario(prestador_valido):
        print("Prestador válido criado com sucesso!")
    else:
        print("Falha ao criar prestador válido.")
    
    print("Tentando criar usuários inválidos...")
    if not controller.create_usuario(condomino_invalido):
        print("Falha ao criar condomino inválido.")
    if not controller.create_usuario(prestador_invalido):
        print("Falha ao criar prestador inválido.")
    
    print("Recuperando usuários...")
    usuarios = controller.get_usuario_por_tipo(Condomino)
    print("Condominos:", usuarios)
    
    prestadores = controller.get_prestador_por_servico(Servico.ELETRICISTA)
    print("Prestadores para Eletricista:", prestadores)
    
    print("Atualizando usuário...")
    condomino_atualizado = Condomino(
        id=1, nome="Ana Atualizada", cpf="12345678900", telefone="999999999", login="ana_login", senha="NovaSenha@123", bloco="B", ap="202"
    )
    if controller.update_usuario(1, condomino_atualizado):
        print("Condomino atualizado com sucesso!")
    
    usuario_atualizado = controller.get_usuario_por_id(1)
    print("Usuário atualizado:", usuario_atualizado)
    
    print("Excluindo usuário...")
    if controller.delete_usuario_por_id(2):
        print("Prestador excluído com sucesso!")

if __name__ == "__main__":
    main()
