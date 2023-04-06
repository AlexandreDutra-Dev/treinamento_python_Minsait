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
                    "Valor inválido para saque. Digite um número válido.")
            if valor <= 0:
                raise ValueError(
                    "Valor inválido para saque. Digite acima de R$0,00.")
            if not self.tem_saldo_suficiente(valor):
              raise ValueError("Saldo insuficiente para realizar o saque.")
            self.saldo -= valor
            print("Saque realizado com sucesso. Saldo: R${:.2f}".format(
                self.saldo))
        except ValueError as erro:
            print(erro)

    def tem_saldo_suficiente(self, valor: float) -> bool:
        return self.saldo >= valor

    def depositar(self, valor: float):
        try:
            if not isinstance(valor, (float, int)):
                raise ValueError(
                    "Valor inválido para depósito. Digite um número válido.")
            if valor <= 0:
                raise ValueError(
                    "Valor inválido para depósito. Digite um a valor acima de R$0,00.")
            self.saldo += valor
            print("Depósito realizado com sucesso. Saldo: R${:.2f}".format(
                self.saldo))
        except ValueError as erro:
            print(erro)

    def verificar_rendimentos(self, frequencia):
      if frequencia == "anual":
          self.saldo += self.saldo * self._taxa_de_rendimento
          print("Rendimento anual: R${:.2f}".format(
              self.saldo * self._taxa_de_rendimento))
      elif frequencia == "mensal":
          self.saldo += self.saldo * self._taxa_de_rendimento / 12
          print("Rendimento mensal: R${:.2f}".format(
              self.saldo * self._taxa_de_rendimento / 12))
      elif frequencia == "diario":
          self.saldo += self.saldo * self._taxa_de_rendimento / 365
          print("Rendimento diário: R${:.2f}".format(
              self.saldo * self._taxa_de_rendimento / 365))
      elif frequencia == "por_hora":
          self.saldo += self.saldo * self._taxa_de_rendimento / 8760
          print("Rendimento por hora: R${:.2f}".format(
              self.saldo * self._taxa_de_rendimento / 8760))
      elif frequencia == "por_minuto":
          self.saldo += self.saldo * self._taxa_de_rendimento / 525600
          print("Rendimento por minuto: R${:.2f}".format(
              self.saldo * self._taxa_de_rendimento / 525600))
      elif frequencia == "por_segundo":
          self.saldo += self.saldo * self._taxa_de_rendimento / 31536000
          print("Rendimento por segundo: R${:.2f}".format(
              self.saldo * self._taxa_de_rendimento / 31536000))
