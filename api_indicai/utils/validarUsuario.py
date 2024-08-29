from validarLogin import ValidarLogin
from validarSenha import ValidarSenha
from ..models.condomino import Condomino
from ..models.prestador import Prestador

class ValidarUsuario:

    @staticmethod
    def validar(usuario):
        erros = []

        if isinstance(usuario, Condomino) or isinstance(usuario, Prestador):
            if not ValidarLogin.validar(usuario.login):
                erros.append("Login inválido!")
            if not ValidarSenha.validar_senha(usuario.senha):
                erros.append("Senha inválida!")

        return (len(erros) == 0, erros)