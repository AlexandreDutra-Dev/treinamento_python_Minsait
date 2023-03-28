from Conta import Conta
class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite: float):
        super().__init__(id_conta, saldo)
        self._limite = limite

    @property
    def limite(self) -> float:
        return self._limite

    @limite.setter
    def limite(self, limite: float):
        self._limite = limite

    def sacar(self, valor: float):
        try:
            if valor <= 0:
                raise ValueError(
                    "Valor inválido para saque. Digite um valor acima de R$0,00.\n")
            elif valor > self.saldo:
                raise ValueError("Saldo insuficiente para saque.\n")
            self.saldo -= valor
            print("Saque realizado com sucesso. Saldo: R${:.2f}.\n".format(
                self.saldo))
        except ValueError as erro:
            print(erro)

    def depositar(self, valor: float):
        try:
            if not isinstance(valor, (float, int)):
                raise TypeError(
                    "Valor inválido para depósito. Digite um número válido.\n")
            if valor <= 0:
                raise ValueError(
                    "Valor inválido para depósito. Digite um valor acima de R$0,00.\n")
            self.saldo += valor
            print("Depósito realizado com sucesso. Saldo: R${:.2f} / Limite: R${:.2f}.\n".format(
                self.saldo, self._limite))
        except (TypeError, ValueError) as erro:
            print(erro)
