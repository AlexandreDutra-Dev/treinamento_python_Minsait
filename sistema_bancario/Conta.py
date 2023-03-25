class Conta:
    def __init__(self, id_conta, saldo):
        self.__id_conta = id_conta
        self.__saldo = saldo

    def get_id_conta(self):
        return self.__id_conta

    def set_id_conta(self, id_conta):
        self.__id_conta = id_conta

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        self.__saldo += valor
