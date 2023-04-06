
from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite: float):
        super().__init__(id_conta, saldo)
        self._limite = limite
        self.__limite_utilizado: float = 0

    @property
    def limite(self) -> float:
        return self._limite

    @limite.setter
    def limite(self, limite: float):
        self._limite = limite

    def sacar(self, valor: float):
        try:
            if not isinstance(valor, (float, int)):
                raise ValueError(
                    "Valor inválido para saque. Digite um número válido.")
            if valor <= 0:
                raise ValueError(
                    "Valor inválido para saque. Digite um valor acima de R$0,00.")
            if not self.tem_saldo_suficiente(valor):
                raise ValueError("Saldo insuficiente para realizar o saque.")

            if self.saldo >= valor:
                self.saldo -= valor
            else:
                self.sacar_do_limite(valor - self.saldo)
            print("Saque realizado com sucesso. Saldo: R${:.2f} / Limite: R${:.2f}".format(
                self.saldo, self._limite))
            if self.__limite_utilizado > 0:
                print("Limite utilizado: R${:.2f}".format(
                    self.__limite_utilizado))
        except ValueError as erro:
            print(erro)

    def tem_saldo_suficiente(self, valor: float) -> bool:
        saldo_disponivel = self.saldo + self._limite
        return saldo_disponivel >= valor

    def sacar_do_limite(self, valor: float):
        self.__limite_utilizado = valor
        self._limite -= self.__limite_utilizado
        self.saldo = 0

    def depositar(self, valor: float):
        try:
            if not isinstance(valor, (float, int)) or valor <= 0:
                raise ValueError(
                    "Valor inválido para depósito. Digite um valor acima de R$0,00.")

            self.__depositar_no_limite(valor)

            if self.__limite_utilizado > 0:
                print("Limite utilizado: R${:.2f}.".format(
                    self.__limite_utilizado))

            print("Depósito realizado com sucesso. Saldo: R${:.2f} / Limite: R${:.2f}".format(
                self.saldo, self._limite))
        except ValueError as erro:
            print(erro)

    def __depositar_no_limite(self, valor: float):
        if self.__limite_utilizado > 0:
            if valor >= self.__limite_utilizado:
                valor -= self.__limite_utilizado
                self._limite += self.__limite_utilizado
                self.__limite_utilizado = 0
            else:
                self.__limite_utilizado -= valor
                self._limite += valor
                valor = 0

        if valor > 0:
            self.saldo += valor
