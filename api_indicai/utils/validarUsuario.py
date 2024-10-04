from api_indicai.utils.validarLogin import ValidarLogin
from api_indicai.utils.validarSenha import ValidarSenha
from api_indicai.models.condomino import Condomino

class ValidarUsuario:

    @staticmethod
    def validar(usuario):
        erros = []

        if isinstance(usuario, Condomino):
            if not ValidarLogin.validar(usuario.login):
                erros.append("Login inválido!")
            
            senha_validator = ValidarSenha()
            if not senha_validator.validar_senha(usuario.senha):
                erros.append("Senha inválida!")

        return (len(erros) == 0, erros)
