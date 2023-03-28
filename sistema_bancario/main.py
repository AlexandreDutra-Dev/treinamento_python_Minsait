"""
Esse arquivo é responsável por inserir os valores de forma automática, caso queira inserir manualmente, utilizar o arquivo insercao_manual.py
Se deseja uma saida mais limpa dos resultados, basta acessar o arquivo resultados_testes.csv que será gerado na pasta sistema_bancario

"""
import csv
from Conta_Corrente import ContaCorrente
from Conta_Poupanca import ContaPoupanca

filename = "sistema_bancario/resultados_testes.csv"


# Teste 1: verificar saldo da conta corrente e o limite
print("------------------------------------------------------\n")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
print("Teste 1: verificar saldo da conta corrente e o limite")
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.saldo))
print("Limite da conta corrente: R${:.2f}".format(conta_corrente.limite))
resultado_1 = f"Saldo da conta corrente: R${conta_corrente.saldo :.2f}\nLimite da conta corrente: R${conta_corrente.limite:.2f}\n"
# Teste 2: fazer um saque e verificar o saldo na conta corrente
print("------------------------------------------------------\n")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
print("Teste 2: fazer um saque e verificar o saldo")
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.saldo))
print("Saque de R$ 230")
conta_corrente.sacar(230)
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.saldo))
print("limite da conta corrente: R${:.2f}".format(conta_corrente.limite))
resultado_2 = f"Saldo da conta corrente: R${conta_corrente.saldo :.2f}\nLimite da conta corrente: R${conta_corrente.limite:.2f}\n"

# Teste 3: fazer um saque e usar o limite na conta corrente
print("------------------------------------------------------\n")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
print("Teste 3: fazer um saque e usar o limite")
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.saldo))
print("Saque de R$ 1200")
conta_corrente.sacar(1200)
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.saldo))
resultado_3 = f"Saldo da conta corrente: R${conta_corrente.saldo :.2f}\nLimite da conta corrente: R${conta_corrente.limite:.2f}\n"


# Teste 4: fazer um saque e ultrapassar o limite na conta corrente
print("------------------------------------------------------\n")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
print("Teste 4: fazer um saque e ultrapassar o limite")
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.saldo))
print("Saque de R$ 1800")
conta_corrente.sacar(1800)
resultado_4 = f"Saldo da conta corrente: R${conta_corrente.saldo :.2f}\nLimite da conta corrente: R${conta_corrente.limite:.2f}\n"

# Teste 5: fazer um depósito e verificar o saldo na conta corrente
print("------------------------------------------------------\n")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
print("Teste 5: fazer um depósito e verificar o saldo")
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.saldo))
print("Depósito de R$ 2500")
conta_corrente.depositar(2500)
print("Saldo da conta corrente: R${:.2f}".format(
    conta_corrente.saldo + conta_corrente.limite))
resultado_5 = f"Saldo da conta corrente: R${conta_corrente.saldo :.2f}\nLimite da conta corrente: R${conta_corrente.limite:.2f}\n"

# Teste 6: verificar saldo da conta poupança e a taxa de rendimento
print("------------------------------------------------------\n")
print("Teste 6: verificar saldo da conta poupança e a taxa de rendimento")
conta_poupanca = ContaPoupanca(
    id_conta=2, saldo=10000, taxa_de_rendimento=2)

print("Saldo da conta poupança: R${:.2f}".format(conta_poupanca.saldo))

print("Rendimento por segundo: R${:.2f}".format(
    conta_poupanca.calcular_rendimento_por_segundo()))
print("Rendimento por minuto: R${:.2f}".format(
    conta_poupanca.calcular_rendimento_por_minuto()))
print("Rendimento por hora: R${:.2f}".format(
    conta_poupanca.calcular_rendimento_por_hora()))
print("Rendimento por dia: R${:.2f}".format(
    conta_poupanca.calcular_rendimento_por_dia()))
print("Rendimento por mês: R${:.2f}".format(
    conta_poupanca.calcular_rendimento_por_mes()))
print("Rendimento por ano: R${:.2f}".format(
    conta_poupanca.calcular_rendimento_por_ano()))
resultado_6 = f"Saldo da conta poupança: R${conta_poupanca.saldo :.2f}\n" \
              f"Rendimento por segundo: R${conta_poupanca.calcular_rendimento_por_segundo():.2f}\n" \
              f"Rendimento por minuto: R${conta_poupanca.calcular_rendimento_por_minuto():.2f}\n" \
              f"Rendimento por hora: R${conta_poupanca.calcular_rendimento_por_hora():.2f}\n" \
              f"Rendimento por mês: R${conta_poupanca.calcular_rendimento_por_mes():.2f}\n" \
              f"Rendimento por ano: R${conta_poupanca.calcular_rendimento_por_ano():.2f}\n"


# Teste 7: fazer um saque e verificar o saldo na conta poupança
print("------------------------------------------------------\n")
print("Teste 7: fazer um saque da conta poupança e verificar o saldo")
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=10)
print("Saldo da conta poupança: R${:.2f}".format(conta_poupanca.saldo))
print("Valor do saque: R$500")
conta_poupanca.sacar(500)
conta_poupanca.saldo
resultado_7 = f"Saldo da conta poupança: R${conta_poupanca.saldo :.2f}\n"

# Teste 8: fazer um depósito e verificar o saldo na conta poupança
print("------------------------------------------------------\n")
print("Teste 8: fazer um depósito e verificar o saldo da conta poupança")
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=10)
print("Saldo da conta poupança: R${:.2f}".format(conta_poupanca.saldo))
print("Valor do depósito: R$2500")
conta_poupanca.depositar(2500)
conta_poupanca.saldo
resultado_8 = f"Saldo da conta poupança: R${conta_poupanca.saldo :.2f}\n"

# Teste 9: fazer um saque e ultrapassar o saldo na conta poupança
print("------------------------------------------------------\n")
print("Teste 9: fazer um saque e ultrapassar o saldo da conta poupança")
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=10)
print("Saldo da conta poupança: R${:.2f}".format(conta_poupanca.saldo))
print("Valor do saque: R$6000")
conta_poupanca.sacar(6000)
resultado_9 = f"Saldo da conta poupança: R${conta_poupanca.saldo :.2f}\n"


# abrir arquivo em modo de escrita
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    # escrever cabeçalho do arquivo
    writer.writerow(['Resultado dos testes'])

    # escrever resultados dos testes
    for i in range(1, 10):
        result = globals().get(f'resultado_{i}')
        writer.writerow([f'Teste {i}', result])

    print(f'Resultados dos testes exportados para o arquivo {filename}.')
