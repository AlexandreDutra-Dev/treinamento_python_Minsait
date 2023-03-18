class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def consultar_saldo(self):
        print("Saldo atual: R${:.2f}".format(self.saldo))


conta_alexandre = ContaBancaria("Alexandre", 1000.25)

conta_alexandre.depositar(1000.00)

conta_alexandre.consultar_saldo()
