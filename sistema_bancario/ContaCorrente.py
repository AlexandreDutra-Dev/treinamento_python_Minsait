from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta, saldo, limite):
        super().__init__(id_conta, saldo)
        self.__limite = limite

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    def sacar(self, valor):
        if (self.get_saldo() + self.__limite) >= valor:
            self.set_saldo(self.get_saldo() - valor)
            return True
        else:
            return False
