
from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite: float):
        super().__init__(id_conta, saldo)
        self._limite = limite
        self.__limite_utilizado: float = 0

    @property
    def limite(self) -> float:
        return self._limite

    @limite.setter
    def limite(self, limite: float):
        self._limite = limite

    def sacar(self, valor: float):
      if not isinstance(valor, (float, int)):
          print("Valor inválido para saque. Digite um número válido.\n")
          return
      if valor <= 0:
          print("Valor inválido para saque. Digite um valor acima de R$0,00.\n")
          return

      if not self.tem_saldo_suficiente(valor):
          print("Saldo insuficiente para realizar o saque.\n")
          return

      if self.saldo >= valor:
          self.saldo -= valor
      else:
          self.sacar_do_limite(valor - self.saldo)

      print("Saque realizado com sucesso. Saldo: R${:.2f} / Limite: R${:.2f}.\n".format(
          self.saldo, self._limite))
      if self.__limite_utilizado > 0:
          print("Limite utilizado: R${:.2f}.\n".format(
              self.__limite_utilizado))

    def tem_saldo_suficiente(self, valor: float) -> bool:
        saldo_disponivel = self.saldo + self._limite
        return saldo_disponivel >= valor

    def sacar_do_limite(self, valor: float):
        self.__limite_utilizado = valor
        self._limite -= self.__limite_utilizado
        self.saldo = 0

    def depositar(self, valor: float):
      try:
          if not isinstance(valor, (float, int)):
              raise ValueError(
                  "Valor inválido para depósito. Digite um número válido.\n")
          if valor <= 0:
              raise ValueError(
                  "Valor inválido para depósito. Digite um valor acima de R$0,00.\n")
          if self.__limite_utilizado > 0:
              if valor >= self.__limite_utilizado:
                  valor -= self.__limite_utilizado
                  self._limite += self.__limite_utilizado
                  self.__limite_utilizado = 0
              else:
                  self.__limite_utilizado -= valor
                  self._limite += valor
                  valor = 0
          if valor > 0:
              self.saldo += valor
          print("Depósito realizado com sucesso. Saldo: R${:.2f} / Limite: R${:.2f}.\n".format(
              self.saldo, self._limite))
      except ValueError as erro:
          print(erro)
