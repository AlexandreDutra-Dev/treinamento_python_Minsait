class Conta:
    def __init__(self, id_conta: int, saldo: float) -> None:
        self._id_conta = id_conta
        self._saldo = saldo

    def get_id_conta(self) -> int:
        return self._id_conta

    def set_id_conta(self, id_conta: int) -> None:
        self._id_conta = id_conta

    def get_saldo(self) -> float:
        return self._saldo

    def set_saldo(self, saldo: float):
        self._saldo = saldo

    def sacar():
        pass

    def depositar():
        pass
