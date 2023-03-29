from abc import ABC, abstractmethod
class Conta:
    def __init__(self, id_conta: int, saldo: float):
        self._id_conta = id_conta
        self._saldo = saldo

    @property
    def id_conta(self) -> int:
        return self._id_conta

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, saldo: float):
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor: float):
        pass

    @abstractmethod
    def depositar(self, valor: float):
        pass
