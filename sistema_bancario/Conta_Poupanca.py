from Conta import Conta

SEGUNDOS_EM_ANO = 31536000
MINUTOS_EM_ANO = 525600
HORAS_EM_ANO = 8760
DIAS_EM_ANO = 365


class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_de_rendimento: float):
        super().__init__(id_conta, saldo)
        self.__taxa_de_rendimento = taxa_de_rendimento

    @property
    def taxa_de_rendimento(self) -> float:
        return self.__taxa_de_rendimento

    @taxa_de_rendimento.setter
    def taxa_de_rendimento(self, taxa_de_rendimento: float) -> None:
        self.__taxa_de_rendimento = taxa_de_rendimento

    def sacar(self, valor: float):
        if valor > self._saldo:
            print("Saldo insuficiente para realizar o saque")
        else:
            try:
                self._saldo -= valor
                print("Saque realizado com sucesso. Novo saldo: R${:.2f}".format(
                    self._saldo))
            except ValueError as e:
                print(e)

    def depositar(self, valor: float):
        self._saldo += valor
        print("Depósito realizado com sucesso. Novo saldo: R${:.2f}".format(
            self._saldo))

    def calcular_rendimento_por_segundo(self, valor_simulacao=None) -> float:
        if valor_simulacao is not None:
            return valor_simulacao * ((1 + self.__taxa_de_rendimento / 100) ** (1 / SEGUNDOS_EM_ANO) - 1)
        else:
            return self._saldo * ((1 + self.__taxa_de_rendimento / 100) ** (1 / SEGUNDOS_EM_ANO) - 1)

    def calcular_rendimento_por_minuto(self, valor_simulacao=None) -> float:
        if valor_simulacao is not None:
            return valor_simulacao * ((1 + self.__taxa_de_rendimento / 100) ** (1 / MINUTOS_EM_ANO) - 1)
        else:
            return self._saldo * ((1 + self.__taxa_de_rendimento / 100) ** (1 / MINUTOS_EM_ANO) - 1)

    def calcular_rendimento_por_hora(self, valor_simulacao=None) -> float:
        if valor_simulacao is not None:
            return valor_simulacao * ((1 + self.__taxa_de_rendimento / 100) ** (1 / HORAS_EM_ANO) - 1)
        else:
            return self._saldo * ((1 + self.__taxa_de_rendimento / 100) ** (1 / HORAS_EM_ANO) - 1)

    def calcular_rendimento_por_dia(self, valor_simulacao=None) -> float:
        if valor_simulacao is not None:
            return valor_simulacao * ((1 + self.__taxa_de_rendimento / 100) ** (1 / DIAS_EM_ANO) - 1)
        else:
            return self._saldo * ((1 + self.__taxa_de_rendimento / 100) ** (1 / DIAS_EM_ANO) - 1)

    def calcular_rendimento_por_mes(self, valor_simulacao=None) -> float:
        if valor_simulacao is not None:
            return valor_simulacao * self.__taxa_de_rendimento / 1200
        else:
            return self._saldo * self.__taxa_de_rendimento / 1200

    def calcular_rendimento_por_ano(self, valor_simulacao=None) -> float:
        if valor_simulacao is not None:
            return valor_simulacao * self.__taxa_de_rendimento / 100
        else:
            return self._saldo * self.__taxa_de_rendimento / 100
