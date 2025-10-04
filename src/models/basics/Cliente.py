
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        self.transacao = transacao
        self.conta = conta

    def adicionar_conta(self, conta):
        self.conta = conta
        self.contas.append(self.conta)
        return self.contas