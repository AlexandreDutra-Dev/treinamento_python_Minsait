from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta: str, saldo: float, limite: float) -> None:
        super().__init__(id_conta, saldo)
        self.__limite: float = limite
        self.__limite_maximo: float = limite

    def sacar(self, valor: float) -> None:
        try:
            saldo_disponivel: float = self.get_saldo() + self.__limite
            if saldo_disponivel >= valor:
                if self.get_saldo() >= valor:
                    self.set_saldo(self.get_saldo() - valor)
                else:
                    limite_utilizado: float = valor - self.get_saldo()
                    self.set_saldo(0)
                    self.__limite -= limite_utilizado
                print("Saque realizado com sucesso")
                print(f"Limite utilizado: R${limite_utilizado:.2f}")
                available_balance: float = self.__limite + self.get_saldo()
                print(f"Saldo disponivel para saque: R${available_balance:.2f}" if available_balance >=
                      0 else f"Saldo disponivel para saque: -R${abs(available_balance):.2f}")
            else:
                raise ValueError("Saldo insuficiente para realizar o saque.")
        except ValueError as e:
            print(e)

    def depositar(self, valor: float) -> None:
        available_limit: float = self.__limite + self.get_saldo()
        if available_limit + valor <= self.__limite_maximo:
            self.__limite += valor
            print(
                f"Depósito realizado com sucesso. Novo limite: R${self.__limite:.2f}")
        else:
            valor_compensar: float = self.__limite_maximo - available_limit
            self.__limite += valor_compensar
            self.set_saldo(self.get_saldo() + valor - valor_compensar)
            print(
                f"Depósito realizado com sucesso. Limite totalmente compensado. Novo saldo: R${self.get_saldo():.2f}")
            print(f"Novo limite disponível: R${self.__limite:.2f}")

    def get_limite(self) -> float:
        return self.__limite
