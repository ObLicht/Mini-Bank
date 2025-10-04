from models.basics.Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        if valor <= self.saldo and valor <= self.limite and valor < self.limite_saques:
            self.saldo -= valor
            self._limite += 1
            print("\n=== Saque Realizado com sucesso! ===")
        else:
            print("Saque inválido")

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """