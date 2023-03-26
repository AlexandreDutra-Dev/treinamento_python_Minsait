from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Teste 1: saque acima do saldo + limite em conta corrente
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
print("Saldo inicial: {:.2f}".format(conta_corrente.get_saldo()))

conta_corrente.sacar(valor=2000)

print("Saldo final: {:.2f}".format(conta_corrente.get_saldo()))

# Teste 2: saque, depósito e verificação de rendimento em conta poupança
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=2)
print("Saldo inicial: {:.2f}, rendimento anual: {:.2f}".format(
    conta_poupanca.get_saldo(), conta_poupanca.verificar_rendimento_ao_ano()))

conta_poupanca.sacar(valor=2000)
print("Saldo após saque: {:.2f}, rendimento anual: {:.2f}".format(
    conta_poupanca.get_saldo(), conta_poupanca.verificar_rendimento_ao_ano()))

conta_poupanca.depositar(valor=1000)
print("Saldo após depósito: {:.2f}, rendimento anual: {:.2f}".format(
    conta_poupanca.get_saldo(), conta_poupanca.verificar_rendimento_ao_ano()))

# Teste 3: depósito em conta corrente
conta_corrente = Conta(id_conta=3, saldo=2000)
print("Saldo inicial: {:.2f}".format(conta_corrente.get_saldo()))

conta_corrente.depositar(valor=500)
print("Saldo após depósito: {:.2f}".format(conta_corrente.get_saldo()))

# Teste 4: saque em conta corrente
conta_corrente.sacar(valor=1000)
print("Saldo após saque: {:.2f}".format(conta_corrente.get_saldo()))

# Teste 5: saque em conta poupança com saldo insuficiente
try:
    conta_poupanca.sacar(valor=10000)
except ValueError as error:
    print(error)

# Teste 6: saque em conta corrente com saldo insuficiente
try:
    conta_corrente.sacar(valor=10000)
except ValueError as error:
    print(error)
