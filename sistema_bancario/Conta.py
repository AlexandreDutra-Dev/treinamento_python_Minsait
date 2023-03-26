class Conta:
    def __init__(self, id_conta: int, saldo: float):
        self._id_conta = id_conta
        self._saldo = saldo

    def get_id_conta(self) -> int:
        return self._id_conta

    def set_id_conta(self, id_conta: int):
        self._id_conta = id_conta

    def get_saldo(self) -> float:
        return self._saldo

    def set_saldo(self, saldo: float):
        self._saldo = saldo

    def sacar(self, valor: float):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            raise ValueError("Saldo insuficiente")

    def depositar(self, valor: float):
        self._saldo += valor
        print("Depósito realizado com sucesso. Novo saldo: R${:.2f}".format(
            self._saldo))
