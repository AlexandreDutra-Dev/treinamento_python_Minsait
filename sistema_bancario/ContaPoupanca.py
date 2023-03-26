from Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_de_rendimento: float):
        super().__init__(id_conta, saldo)
        self.__taxa_de_rendimento = taxa_de_rendimento

    def sacar(self, valor: float):
        try:
            if self.get_saldo() >= valor:
                self.set_saldo(self.get_saldo() - valor)
                print("Saque realizado com sucesso. Novo saldo: R${:.2f}".format(
                    self._saldo))
            else:
                raise ValueError("Saldo insuficiente para realizar o saque.")
        except ValueError as e:
            print(e)

    def get_rendimento_anual(self):
        return self.get_saldo() * self.__taxa_de_rendimento / 100

    def get_rendimento_por_periodo(self, periodo: str):
        segundos_em_ano = 31536000
        minutos_em_ano = segundos_em_ano / 60
        horas_em_ano = minutos_em_ano / 60
        dias_em_ano = horas_em_ano / 24

        if periodo == 'segundos':
            return self.get_saldo() * self.__taxa_de_rendimento / 100 / segundos_em_ano
        elif periodo == 'minutos':
            return self.get_saldo() * self.__taxa_de_rendimento / 100 / minutos_em_ano
        elif periodo == 'horas':
            return self.get_saldo() * self.__taxa_de_rendimento / 100 / horas_em_ano
        elif periodo == 'dias':
            return self.get_saldo() * self.__taxa_de_rendimento / 100 / dias_em_ano
        elif periodo == 'meses':
            return self.get_saldo() * self.__taxa_de_rendimento / 100 / 12
        elif periodo == 'anos':
            return self.get_saldo() * self.__taxa_de_rendimento / 100
