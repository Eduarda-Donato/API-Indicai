from abc import ABC, abstractmethod
from api_indicai.repositories.usuarioRepositoryInMemory import UsuarioRepositoryInMemory
from api_indicai.repositories.avaliacaoRepository import AvaliacaoRepository

class Relatorio(ABC):
    def __init__(self, usuario_repository: UsuarioRepositoryInMemory, avaliacao_repository: AvaliacaoRepository):
        self.usuario_repository = usuario_repository
        self.avaliacao_repository = avaliacao_repository

    def gerar_relatorio(self):
        dados = self.obter_dados()
        self.processar_dados(dados)
        conteudo = self.gerar_conteudo(dados)
        self.exportar(conteudo)

    def obter_dados(self):
        # Coletando dados dos repositórios de usuários e avaliações
        dados = {
            'usuarios_ativos': self.usuario_repository.contar_usuarios(),
            'avaliacoes': self.avaliacao_repository.contar_avaliacoes()  # Usando o método count para avaliações
        }
        return dados

    def processar_dados(self, dados):
        pass

    @abstractmethod
    def gerar_conteudo(self, dados):
        pass

    @abstractmethod
    def exportar(self, conteudo):
        pass
