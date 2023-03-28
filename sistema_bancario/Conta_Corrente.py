from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta: str, saldo: float, limite: float) -> None:
        super().__init__(id_conta, saldo)
        self.__limite: float = limite
        self.__limite_maximo: float = limite
        self.__limite_utilizado: float = 0

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, limite: float) -> None:
        self.__limite = limite

    def sacar(self, valor: float) -> None:
        saldo_disponivel: float = self.saldo + self.__limite
        if saldo_disponivel >= valor:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                self.__limite_utilizado = valor - self.saldo
                self.saldo = 0
                self.__limite -= self.__limite_utilizado
            print("Saque realizado com sucesso")
            if self.__limite_utilizado > 0:
                print(f"Limite utilizado: R${self.__limite_utilizado:.2f}")
            balancosaldo: float = self.__limite + self.saldo
            saldo_saque: float = abs(balancosaldo)
            sinal: str = '' if balancosaldo >= 0 else '-'
            print(f"Saldo disponivel para saque: {sinal}R${saldo_saque:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def depositar(self, valor: float) -> None:
        if valor > self.saldo:
            valor_compensar: float = valor - self.saldo
            if self.__limite + valor_compensar <= self.__limite_maximo:
                self.__limite += valor_compensar
                self.saldo(valor)
                print(
                    f"Depósito realizado com sucesso. Limite compensado. Novo limite: R${self.__limite:.2f}")
            else:
                valor_compensar: float = self.__limite_maximo - self.__limite
                self.__limite += valor_compensar
                self._saldo = self._saldo + valor - valor_compensar

                print(
                    f"Depósito realizado com sucesso. Novo saldo: R${self.saldo :.2f}")
                print(f"Limite disponivel: R${self.__limite:.2f}")
        else:
            self.saldo(self.saldo + valor)
            print(
                f"Depósito realizado com sucesso. Novo saldo: R${self.saldo :.2f}")
            print(f"Limite disponível: R${self.__limite:.2f}")
