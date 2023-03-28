from Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_de_rendimento: float):
        super().__init__(id_conta, saldo)
        self._taxa_de_rendimento = taxa_de_rendimento

    @property
    def taxa_de_rendimento(self) -> float:
        return self._taxa_de_rendimento

    @taxa_de_rendimento.setter
    def taxa_de_rendimento(self, taxa_de_rendimento: float):
        self._taxa_de_rendimento = taxa_de_rendimento

    def verificar_rendimento_anual(self):
        print("Rendimento anual: R${:.2f}".format(
            self.saldo * self._taxa_de_rendimento)
        )
        return self.saldo * self._taxa_de_rendimento

    def verificar_rendimento_mensal(self):
        print("Rendimento mensal: R${:.2f}".format(
            self.saldo * self._taxa_de_rendimento / 12)
        )
        taxa_mensal = self._taxa_de_rendimento / 12
        return self.saldo * taxa_mensal

    def verificar_rendimento_diario(self):
        print("Rendimento diário: R${:.2f}".format(
            self.saldo * self._taxa_de_rendimento / 365)
        )
        taxa_diaria = self._taxa_de_rendimento / 365
        return self.saldo * taxa_diaria

    def verificar_rendimento_por_segundo(self):
        print("Rendimento por segundo: R${:.2f}".format(
            self.saldo * self._taxa_de_rendimento / (365 * 24 * 60 * 60))
        )
        taxa_por_segundo = self._taxa_de_rendimento / (365 * 24 * 60 * 60)
        return self.saldo * taxa_por_segundo

    def verificar_rendimento_por_minuto(self):
        print("Rendimento por minuto: R${:.2f}".format(
            self.saldo * self._taxa_de_rendimento / (365 * 24 * 60))
        )
        taxa_por_minuto = self._taxa_de_rendimento / (365 * 24 * 60)
        return self.saldo * taxa_por_minuto

    def verificar_rendimento_por_hora(self):
        print("Rendimento por hora: R${:.2f}".format(
            self.saldo * self._taxa_de_rendimento / (365 * 24))
        )
        taxa_por_hora = self._taxa_de_rendimento / (365 * 24)
        return self.saldo * taxa_por_hora

    def sacar(self, valor: float):
        try:
            if valor <= 0:
                raise ValueError(
                    "Valor inválido para saque. Digite um valor positivo.\n")
            elif valor > self.saldo:
                raise ValueError("Saldo insuficiente para saque.\n")
            self.saldo -= valor
            print("Saque realizado com sucesso. Saldo: R${:.2f}.\n".format(
                self.saldo))
        except ValueError as erro:
            print(erro)

    def depositar(self, valor: float):
        try:
            if not isinstance(valor, (float, int)):
                raise TypeError(
                    "Valor inválido para depósito. Digite um número válido.\n")
            if valor <= 0:
                raise ValueError(
                    "Valor inválido para depósito. Digite um a valor acima de R$0,00.\n")
            self.saldo += valor
            print("Depósito realizado com sucesso. Saldo: R${:.2f}.\n".format(
                self.saldo))
        except (TypeError, ValueError) as erro:
            print(erro)
