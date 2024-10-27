from fpdf import FPDF
from api_indicai.relatorios.Relatorio import Relatorio

class RelatorioPDF(Relatorio):
    def gerar_conteudo(self, dados):
        conteudo = (
            "Relatório de Estatísticas\n"
            f"Usuários: {dados['usuarios']}\n"
            f"Número de avaliações: {dados['avaliacoes']}\n"
        )
        return conteudo

    def exportar(self, conteudo):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.multi_cell(0, 10, conteudo)
        pdf.output('relatorio.pdf')
        print("Relatório PDF gerado com sucesso!")
