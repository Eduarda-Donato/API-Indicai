from api_indicai.relatorios.Relatorio import Relatorio

class RelatorioHTML(Relatorio):
    def gerar_conteudo(self, dados):
        html = f"""
        <h1>Relatório de Estatísticas</h1>
        <p>Usuários: {dados['usuarios']}</p>
        <p>Número de avaliações: {dados['avaliacoes']}</p>
        """
        return html

    def exportar(self, conteudo):
        with open('relatorio.html', 'w') as file:
            file.write(conteudo)
        print("Relatório HTML gerado com sucesso!")

