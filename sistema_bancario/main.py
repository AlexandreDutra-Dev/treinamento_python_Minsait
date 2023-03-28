from Conta_Corrente import ContaCorrente
from Conta_Poupanca import ContaPoupanca

# Cria uma conta corrente com um saldo inicial de R$ 1000,00 e um limite de R$ 500,00
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)

# Cria uma conta poupança com um saldo inicial de R$ 5000,00 e uma taxa de rendimento de 12% ao ano
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=12)

# Testes de conta corrente
conta_corrente.depositar(500)
conta_corrente.depositar(0)
conta_corrente.depositar(-500)
conta_corrente.depositar("abc22")
conta_corrente.sacar(500)
conta_corrente.sacar(0)
conta_corrente.sacar(-500)

print("--------------------------------------------.\n")

# Testes de conta poupança
conta_poupanca.depositar(500)
conta_poupanca.depositar(0)
conta_poupanca.depositar(-500)
conta_poupanca.depositar("abc22")
conta_poupanca.sacar(2500)
conta_poupanca.sacar(4000)
conta_poupanca.sacar(0)
conta_poupanca.sacar(-500)

# mostar o rendimento da conta poupança
print("Teste de rendimento da conta poupança")
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=0.12)
conta_poupanca.verificar_rendimento_por_segundo()
conta_poupanca.verificar_rendimento_por_minuto()
conta_poupanca.verificar_rendimento_por_hora()
conta_poupanca.verificar_rendimento_diario()
conta_poupanca.verificar_rendimento_mensal()
conta_poupanca.verificar_rendimento_anual()
