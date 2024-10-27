from api_indicai.adapters.senhaInterface import SenhaInterface
from api_indicai.services.externalPasswordGenerator import ExternalPasswordGenerator

class SenhaAdapter(SenhaInterface):
    def __init__(self):
        self.servico = ExternalPasswordGenerator()

    def gerar_senha(self) -> str:
        return self.servico.gerar()