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
            saldo_disponivel = self.saldo + self._limite
            if valor > saldo_disponivel:
                raise ValueError("Saldo e limite insuficientes para saque.\n")
            if valor > self.saldo:
                self._limite -= valor - self.saldo
                self.saldo = 0
            else:
                self.saldo -= valor
            print("Saque realizado com sucesso. Saldo: R${:.2f} / Limite: R${:.2f}.\n".format(
                self.saldo, self._limite))
        except ValueError as erro:
            print(erro)

    def depositar(self, valor: float):
        try:
            if not isinstance(valor, (float, int)):
                raise ValueError(
                    "Valor inválido para depósito. Digite um número válido.\n")
            if valor <= 0:
                raise ValueError(
                    "Valor inválido para depósito. Digite um valor acima de R$0,00.\n")
            self.saldo += valor
            print("Depósito realizado com sucesso. Saldo: R${:.2f} / Limite: R${:.2f}.\n".format(
                self.saldo, self._limite))
        except ValueError as erro:
            print(erro)
