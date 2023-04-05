from Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_de_rendimento: float):
        super().__init__(id_conta, saldo)
        self._taxa_de_rendimento = taxa_de_rendimento / 100

    @property
    def taxa_de_rendimento(self) -> float:
        return self._taxa_de_rendimento

    @taxa_de_rendimento.setter
    def taxa_de_rendimento(self, taxa_de_rendimento: float):
        self._taxa_de_rendimento = taxa_de_rendimento

    def sacar(self, valor: float):
        try:
            if not isinstance(valor, (float, int)):
                raise ValueError(
                    "Valor inválido para saque. Digite um número válido.\n")
            if valor <= 0:
                raise ValueError(
                    "Valor inválido para saque. Digite acima de R$0,00.\n")
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
                raise ValueError(
                    "Valor inválido para depósito. Digite um número válido.\n")
            if valor <= 0:
                raise ValueError(
                    "Valor inválido para depósito. Digite um a valor acima de R$0,00.\n")
            self.saldo += valor
            print("Depósito realizado com sucesso. Saldo: R${:.2f}.\n".format(
                self.saldo))
        except ValueError as erro:
            print(erro)

    def verificar_rendimentos(self, frequencia):
      if frequencia == "anual":
          taxa = self._taxa_de_rendimento
          divisor = 1
      elif frequencia == "mensal":
          taxa = self._taxa_de_rendimento / 12
          divisor = 12
      elif frequencia == "diaria":
          taxa = self._taxa_de_rendimento / 365
          divisor = 365
      elif frequencia == "por_segundo":
          taxa = self._taxa_de_rendimento / (365 * 24 * 60 * 60)
          divisor = 365 * 24 * 60 * 60
      elif frequencia == "por_minuto":
          taxa = self._taxa_de_rendimento / (365 * 24 * 60)
          divisor = 365 * 24 * 60
      elif frequencia == "por_hora":
          taxa = self._taxa_de_rendimento / (365 * 24)
          divisor = 365 * 24
      else:
          print("Frequência inválida")
          return 0

      rendimento = self.saldo * taxa / divisor
      print("Rendimento {}: R${:.2f}".format(
          frequencia.capitalize(), rendimento))
      return rendimento
