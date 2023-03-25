from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Teste 1: saque acima do saldo + limite em conta corrente
conta_corrente = ContaCorrente(1, 1000, 500)
print(f"Saldo inicial: {conta_corrente.get_saldo()}")

conta_corrente.sacar(1500)

print(f"Saldo final: {conta_corrente.get_saldo()}")

# Teste 2: saque, depósito e verificação de rendimento em conta poupança
conta_poupanca = ContaPoupanca(2, 5000, 2)
print(
    f"Saldo inicial: {conta_poupanca.get_saldo()}, rendimento anual: {conta_poupanca.verificar_rendimento_ao_ano()}")

conta_poupanca.sacar(2000)
print(
    f"Saldo após saque: {conta_poupanca.get_saldo()}, rendimento anual: {conta_poupanca.verificar_rendimento_ao_ano()}")

conta_poupanca.depositar(1000)
print(
    f"Saldo após depósito: {conta_poupanca.get_saldo()}, rendimento anual: {conta_poupanca.verificar_rendimento_ao_ano()}")

# Teste 3: depósito em conta comum
conta_comum = Conta(3, 2000)
print(f"Saldo inicial: {conta_comum.get_saldo()}")

conta_comum.depositar(500)
print(f"Saldo após depósito: {conta_comum.get_saldo()}")

# Teste 4: saque em conta comum
conta_comum.sacar(1000)
print(f"Saldo após saque: {conta_comum.get_saldo()}")

# Teste 5: saque em conta poupança com saldo insuficiente
conta_poupanca.sacar(6000)

# Teste 6: saque em conta corrente com saldo insuficiente
conta_corrente.sacar(2000)
