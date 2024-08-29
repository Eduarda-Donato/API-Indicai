from password_strength import PasswordPolicy

class ValidarSenha:
    policy = PasswordPolicy.from_names(
        length = 8,        
        uppercase = 1,   
        numbers = 1,        
        special = 1, 
        nonletters = 1 
    )

    def validar_senha(self, senha: str) -> bool:
        try:
            self.policy.test(senha)
            return True
        except Exception as e:
            print(f"Senha inválida: {e}")
            return False
