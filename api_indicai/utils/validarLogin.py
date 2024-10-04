import re

class ValidarLogin:
    
    @staticmethod
    def validar(login: str) -> bool:
        if not login:
            return False
        if len(login) < 5:
            return False
        if not re.match(r'^[a-zA-Z0-9_]+$', login):
            return False
        return True
