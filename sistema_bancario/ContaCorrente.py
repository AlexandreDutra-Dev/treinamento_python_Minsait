from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta: str, saldo: float, limite: float):
        super().__init__(id_conta, saldo)
        self.__limite = limite
        self.__limite_maximo = limite

    def sacar(self, valor):
        try:
            if self.get_saldo() + self.__limite >= valor:
                if self.get_saldo() >= valor:
                    self.set_saldo(self.get_saldo() - valor)
                else:
                    limite_utilizado = valor - self.get_saldo()
                    self.set_saldo(0)
                    self.__limite -= limite_utilizado
                print("Saque realizado com sucesso")
                print("Limite utilizado: R${:.2f}".format(limite_utilizado))
                available_balance = self.__limite + self.get_saldo()
                if available_balance >= 0:
                    print("Saldo disponivel para saque: R${:.2f}".format(
                        available_balance))
                else:
                    print(
                        "Saldo disponivel para saque: -R${:.2f}".format(abs(available_balance)))
            else:
                raise ValueError("Saldo insuficiente para realizar o saque.")
        except ValueError as e:
            print(e)

    def depositar(self, valor: float):
        available_limit = self.__limite + self.get_saldo()
        if available_limit + valor <= self.__limite_maximo:
            self.__limite += valor
            print("Depósito realizado com sucesso. Novo limite: R${:.2f}".format(
                self.__limite))
        else:
            valor_compensar = self.__limite_maximo - available_limit
            self.__limite += valor_compensar
            self.set_saldo(self.get_saldo() + valor - valor_compensar)
            print("Depósito realizado com sucesso. Limite totalmente compensado. Novo saldo: R${:.2f}".format(
                self.get_saldo()))
            print("Novo limite disponível: R${:.2f}".format(self.__limite))

    def get_limite(self):
        return self.__limite
