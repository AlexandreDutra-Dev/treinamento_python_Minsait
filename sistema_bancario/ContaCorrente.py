from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta, saldo, limite):
        super().__init__(id_conta, saldo)
        self.__limite = limite

    def sacar(self, valor):
        try:
            if self.get_saldo() + self.__limite >= valor:
                self.set_saldo(self.get_saldo() - valor)
                print(
                    f"Saque realizado com sucesso. Novo saldo: {self.get_saldo()}")
            else:
                raise ValueError("Saldo insuficiente para realizar o saque.")
        except ValueError as e:
            print(e)
