from api_indicai.adapters.senhaAdapter import SenhaAdapter

class SenhaService:
    def __init__(self):
        self.adapter = SenhaAdapter()

    def obter_senha(self) -> str:
        return self.adapter.gerar_senha()
