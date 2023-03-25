from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Criando uma conta comum
conta1 = Conta(1, 1000)
print(f'Conta {conta1.get_id_conta()}: Saldo = {conta1.get_saldo()}')

# Sacando dinheiro da conta comum
conta1.sacar(500)
print(f'Conta {conta1.get_id_conta()}: Saldo = {conta1.get_saldo()}')

# Depositando dinheiro na conta comum
conta1.depositar(1000)

# Criando uma conta corrente
conta2 = ContaCorrente(2, 500, 1000)
print(f'Conta {conta2.get_id_conta()}: Saldo = {conta2.get_saldo()}, Limite = {conta2.get_limite()}')

# Sacando dinheiro da conta corrente com limite
conta2.sacar(1000)
print(f'Conta {conta2.get_id_conta()}: Saldo = {conta2.get_saldo()}, Limite = {conta2.get_limite()}')

# Tentando sacar um valor maior do que o limite
conta2.sacar(1500)
print(f'Conta {conta2.get_id_conta()}: Saldo = {conta2.get_saldo()}, Limite = {conta2.get_limite()}')

# Criando uma conta poupança
conta3 = ContaPoupanca(3, 10000, 2.5)
if isinstance(conta3, ContaPoupanca):
    print(f'Conta {conta3.get_id_conta()}: Saldo = {conta3.get_saldo()}, Taxa de rendimento = {conta3.verificar_rendimento_ao_ano()}')
else:
    print(
        f'Conta {conta3.get_id_conta()}: Saldo = {conta3.get_saldo()}, Limite = {conta3.get_limite()}')


# Verificando o rendimento anual da conta poupança
rendimento = conta3.verificar_rendimento_ao_ano()
print(f'Rendimento anual da conta {conta3.get_id_conta()}: {rendimento:.2f}')
