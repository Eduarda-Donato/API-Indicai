import random
import string

class ExternalPasswordGenerator:
    def gerar(self, tamanho: int = 12) -> str:
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        return senha