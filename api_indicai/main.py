# main.py
import sys
import os
from utils.validarLogin import ValidarLogin
from utils.validarSenha import ValidarSenha
from utils.validarUsuario import ValidarUsuario
from models.condomino import Condomino
from models.prestador import Prestador
from enums.servico import Servico

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    # Criar instâncias de exemplo
    condomino_valido = Condomino(
        id=1, nome="Ana", cpf="12345678900", telefone="999999999", login="ana_login", senha="Senha@123", bloco="A", ap="101"
    )
    prestador_valido = Prestador(
        id=2, nome="Carlos", cpf="09876543211", telefone="888888888", login="carlos_login", senha="Senha@456", tipoServico=Servico.ELETRICISTA
    )

    condomino_invalido = Condomino(
        id=3, nome="Lucas", cpf="98765432100", telefone="777777777", login="lu", senha="123", bloco="B", ap="202"
    )
    prestador_invalido = Prestador(
        id=4, nome="Maria", cpf="12345678999", telefone="666666666", login="maria_login", senha="abc", tipoServico=Servico.LIMPEZA
    )

    # Testar validação para Condomino e Prestador válidos
    valido, erros = ValidarUsuario.validar(condomino_valido)
    print(f"Condomino válido: {valido}, Erros: {erros}")

    valido, erros = ValidarUsuario.validar(prestador_valido)
    print(f"Prestador válido: {valido}, Erros: {erros}")

    # Testar validação para Condomino e Prestador inválidos
    valido, erros = ValidarUsuario.validar(condomino_invalido)
    print(f"Condomino inválido: {valido}, Erros: {erros}")

    valido, erros = ValidarUsuario.validar(prestador_invalido)
    print(f"Prestador inválido: {valido}, Erros: {erros}")

if __name__ == "__main__":
    main()
