from Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, id_conta, saldo, taxa_de_rendimento):
        super().__init__(id_conta, saldo)
        self.__taxa_de_rendimento = taxa_de_rendimento

    def sacar(self, valor):
        try:
            if self.get_saldo() >= valor:
                self.set_saldo(self.get_saldo() - valor)
                print(
                    f"Saque realizado com sucesso. Novo saldo: {self.get_saldo()}")
            else:
                raise ValueError("Saldo insuficiente para realizar o saque.")
        except ValueError as e:
            print(e)

    def verificar_rendimento_ao_ano(self):
        return self.get_saldo() * self.__taxa_de_rendimento / 100
