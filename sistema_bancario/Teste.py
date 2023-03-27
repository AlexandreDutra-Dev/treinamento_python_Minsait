from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=2)

# Teste 1: verificar saldo da conta corrente e o limite
print("Teste 1: verificar saldo da conta corrente e o limite")
print(conta_corrente.get_saldo())
print(conta_corrente.get_limite())

# Teste 2: fazer um saque e verificar o saldo na conta corrente
print("Teste 2: fazer um saque e verificar o saldo")
conta_corrente.sacar(500)

# Teste 3: fazer um saque e usar o limite na conta corrente
print("Teste 3: fazer um saque e usar o limite")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
conta_corrente.sacar(1200)

# Teste 4: fazer um saque e ultrapassar o limite na conta corrente
print("Teste 4: fazer um saque e ultrapassar o limite")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
conta_corrente.sacar(1800)

# Teste 5: fazer um depósito e verificar o saldo na conta corrente
print("Teste 5: fazer um depósito e verificar o saldo")
conta_corrente.depositar(2500)
conta_corrente.get_saldo()

# Teste 6: verificar saldo da conta poupança e a taxa de rendimento
print("Teste 6: verificar saldo da conta poupança e a taxa de rendimento")
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=2)
print(conta_poupanca.get_saldo())
print(conta_poupanca.get_rendimento_por_periodo("segundos"))
print(conta_poupanca.get_rendimento_por_periodo("minutos"))
print(conta_poupanca.get_rendimento_por_periodo("horas"))
print(conta_poupanca.get_rendimento_por_periodo("dias"))
print(conta_poupanca.get_rendimento_por_periodo("meses"))
print(conta_poupanca.get_rendimento_por_periodo("anos"))


# Teste 6: fazer um saque e verificar o saldo na conta poupança
print("Teste 6: fazer um saque e verificar o saldo")
conta_poupanca.sacar(500)
