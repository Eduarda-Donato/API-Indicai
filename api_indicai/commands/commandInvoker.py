from commands.commandInterface import CommandInterface

class CommandInvoker:
    def __init__(self):
        self.historico = []  # Para armazenar o histórico de comandos executados

    def execute_command(self, command: CommandInterface):
        resultado = command.executar()
        self.historico.append(command)  # Armazena o comando executado no histórico
        return resultado