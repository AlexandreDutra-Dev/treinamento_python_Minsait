from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta: str, saldo: float, limite: float) -> None:
        super().__init__(id_conta, saldo)
        self.__limite: float = limite
        self.__limite_maximo: float = limite
        self.__limite_utilizado: float = 0

    def sacar(self, valor: float) -> None:
        saldo_disponivel: float = self.get_saldo() + self.__limite
        if saldo_disponivel >= valor:
            if self.get_saldo() >= valor:
                self.set_saldo(self.get_saldo() - valor)
            else:
                self.__limite_utilizado = valor - self.get_saldo()
                self.set_saldo(0)
                self.__limite -= self.__limite_utilizado
            print("Saque realizado com sucesso")
            if self.__limite_utilizado > 0:
                print(f"Limite utilizado: R${self.__limite_utilizado:.2f}")
            balanco_saldo: float = self.__limite + self.get_saldo()
            saldo_saque: float = abs(balanco_saldo)
            sinal: str = '' if balanco_saldo >= 0 else '-'
            print(f"Saldo disponivel para saque: {sinal}R${saldo_saque:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def depositar(self, valor: float) -> None:
        if valor > self.get_saldo():
            valor_compensar: float = valor - self.get_saldo()
            if self.__limite + valor_compensar <= self.__limite_maximo:
                self.__limite += valor_compensar
                self.set_saldo(valor)
                print(
                    f"Depósito realizado com sucesso. Limite compensado. Novo limite: R${self.__limite:.2f}")
            else:
                valor_compensar: float = self.__limite_maximo - self.__limite
                self.__limite += valor_compensar
                self.set_saldo(self.get_saldo() + valor - valor_compensar)
                print(
                    f"Depósito realizado com sucesso. Novo saldo: R${self.get_saldo():.2f}")
                print(f"Limite disponivel: R${self.__limite:.2f}")
        else:
            self.set_saldo(self.get_saldo() + valor)
            print(
                f"Depósito realizado com sucesso. Novo saldo: R${self.get_saldo():.2f}")
            print(f"Limite disponível: R${self.__limite:.2f}")

    def get_limite(self) -> float:
        return self.__limite

    def get_saldo(self) -> float:
        return self._saldo

    def set_saldo(self, saldo: float) -> None:
        self._saldo = saldo
