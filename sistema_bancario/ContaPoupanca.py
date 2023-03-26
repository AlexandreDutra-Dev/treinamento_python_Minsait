from Conta import Conta

SEGUNDOS_EM_ANO = 31536000
MINUTOS_EM_ANO = SEGUNDOS_EM_ANO / 60
HORAS_EM_ANO = MINUTOS_EM_ANO / 60
DIAS_EM_ANO = HORAS_EM_ANO / 24

class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_de_rendimento: float):
        super().__init__(id_conta, saldo)
        self.__taxa_de_rendimento = taxa_de_rendimento

    def sacar(self, valor: float):
        try:
            self.set_saldo(self.get_saldo() - valor)
            print("Saque realizado com sucesso. Novo saldo: R${:.2f}".format(
                self.get_saldo()))
        except ValueError as e:
            print(e)

    def get_rendimento_por_periodo(self, periodo: str):
        fatores_conversao = {
            'segundos': SEGUNDOS_EM_ANO,
            'minutos': MINUTOS_EM_ANO,
            'horas': HORAS_EM_ANO,
            'dias': DIAS_EM_ANO,
            'meses': 12,
            'anos': 1
        }
        if periodo in fatores_conversao:
            fator = fatores_conversao[periodo]
            return self.get_saldo() * self.__taxa_de_rendimento / 100 / fator
        else:
            raise ValueError("Período inválido.")
