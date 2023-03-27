class Conta:
    def __init__(self, id_conta: int, saldo: float) -> None:
        self._id_conta = id_conta
        self._saldo = saldo

    @property
    def id_conta(self) -> int:
        return self._id_conta

    @id_conta.setter
    def id_conta(self, id_conta: int) -> None:
        self._id_conta = id_conta

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, saldo: float):
        self._saldo = saldo
