from Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, id_conta, saldo, taxa_de_rendimento):
        super().__init__(id_conta, saldo)
        self.__taxa_de_rendimento = taxa_de_rendimento

    def depositar(self, valor):
        valor_rendimento = valor * self.__taxa_de_rendimento
        valor_total = valor + valor_rendimento
        super().depositar(valor_total)
        print(
            f'Depósito de R$ {valor:.2f} realizado com sucesso na conta {self.get_id_conta()} (rendimento de R$ {valor_rendimento:.2f})')

    def verificar_rendimento_ao_ano(self):
        return self.get_saldo() * self.__taxa_de_rendimento
