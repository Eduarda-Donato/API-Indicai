import unittest
from api_indicai.enums.servico import Servico
from api_indicai.models.prestador import Prestador
from api_indicai.services.prestadorManager import PrestadorManager

class TestPrestadorManager(unittest.TestCase):

    def setUp(self):
        self.manager = PrestadorManager()
        self.prestador1 = Prestador(
            id=1, nome="Ana", cpf=123456789, telefone="999999999",
            endereco="Rua A", tipoServico=Servico.ELETRICISTA
        )
        self.prestador2 = Prestador(
            id=2, nome="Bruno", cpf=987654321, telefone="888888888",
            endereco="Rua B", tipoServico=Servico.JARDINEIRO
        )
        self.manager.create_prestador(self.prestador1)
        self.manager.create_prestador(self.prestador2)

    def test_adicionar_prestador(self):
        prestador3 = Prestador(
            id=3, nome="Carlos", cpf=112233445, telefone="777777777",
            endereco="Rua C", tipoServico=Servico.ELETRICISTA
        )
        self.manager.create_prestador(prestador3)
        self.assertIn(prestador3, self.manager.read_prestadores())

    def test_atualizar_prestador_por_nome(self):
        novos_dados = Prestador(
            id=2, nome="Bruno", cpf=987654321, telefone="888888888",
            endereco="Rua Z", tipoServico=Servico.JARDINEIRO
        )
        sucesso = self.manager.update_prestador_nome("Bruno", novos_dados)
        self.assertTrue(sucesso)
        prestador_atualizado = self.manager.read_prestador_nome("Bruno")
        self.assertEqual(prestador_atualizado.endereco, "Rua Z")

    def test_remover_prestador_por_nome(self):
        sucesso = self.manager.delete_prestador_nome("Ana")
        self.assertTrue(sucesso)
        prestador_removido = self.manager.read_prestador_nome("Ana")
        self.assertIsNone(prestador_removido)

    def test_listar_prestadores(self):
        prestadores = self.manager.read_prestadores()
        self.assertEqual(len(prestadores), 2)

if __name__ == '__main__':
    unittest.main()
