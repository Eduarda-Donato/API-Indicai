import unittest
from api_indicai.enums.servico import Servico
from api_indicai.models.condomino import Condomino
from api_indicai.models.prestador import Prestador
from api_indicai.services.usuarioManager import UsuarioManager
from api_indicai.utils.criptografarSenha import CriptografarSenha

class TestUsuarioManager(unittest.TestCase):

    def setUp(self):
        # Inicializa o UsuarioManager e cria usuários de exemplo
        self.manager = UsuarioManager()

        # Cria usuários com senhas criptografadas
        self.condomino1 = Condomino(
            id=1, nome="Ana", cpf=123456789, telefone="999999999",
            login="ana123", senha=CriptografarSenha.criptografar("senhaAna"),
            bloco="A", ap="101"
        )
        self.prestador1 = Prestador(
            id=2, nome="Bruno", cpf=987654321, telefone="888888888",
            login="bruno456", senha=CriptografarSenha.criptografar("senhaBruno"),
            tipoServico=Servico.JARDINEIRO
        )
        self.manager.create_usuario(self.condomino1)
        self.manager.create_usuario(self.prestador1)

    def test_adicionar_usuario(self):
        # Testa a adição de um novo usuário
        novo_condomino = Condomino(
            id=3, nome="Carlos", cpf=112233445, telefone="777777777",
            login="carlos789", senha=CriptografarSenha.criptografar("senhaCarlos"),
            bloco="B", ap="202"
        )
        self.manager.create_usuario(novo_condomino)
        self.assertIn(novo_condomino, self.manager.get_usuario_por_tipo(Condomino))

    def test_atualizar_usuario(self):
        # Testa a atualização de um usuário
        novos_dados = Condomino(
            id=1, nome="Ana", cpf=123456789, telefone="999999999",
            login="ana123", senha=CriptografarSenha.criptografar("novaSenhaAna"),
            bloco="A", ap="303"
        )
        sucesso = self.manager.update_usuario(1, novos_dados)
        self.assertTrue(sucesso)
        usuario_atualizado = self.manager.get_usuario_por_id(1)
        self.assertEqual(usuario_atualizado.ap, "303")

    def test_remover_usuario(self):
        # Testa a remoção de um usuário
        sucesso = self.manager.delete_usuario_id(2)
        self.assertTrue(sucesso)
        usuario_removido = self.manager.get_usuario_por_id(2)
        self.assertIsNone(usuario_removido)

    def test_listar_usuarios(self):
        # Testa a listagem de usuários
        condominos = self.manager.get_usuario_por_tipo(Condomino)
        self.assertEqual(len(condominos), 1)
        prestadores = self.manager.get_usuario_por_tipo(Prestador)
        self.assertEqual(len(prestadores), 1)

if __name__ == '__main__':
    unittest.main()
