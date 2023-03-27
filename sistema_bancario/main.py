"""
Esse arquivo é responsável por inserir os valores de forma automática, caso queira inserir manualmente, utilizar o arquivo inserção_manual_de_valores.py
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
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.get_saldo()))
print("Limite da conta corrente: R${:.2f}".format(conta_corrente.get_limite()))
resultado_1 = f"Saldo da conta corrente: R${conta_corrente.get_saldo():.2f}\nLimite da conta corrente: R${conta_corrente.get_limite():.2f}\n"

# Teste 2: fazer um saque e verificar o saldo na conta corrente
print("------------------------------------------------------\n")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
print("Teste 2: fazer um saque e verificar o saldo")
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.get_saldo()))
print("Saque de R$ 230")
conta_corrente.sacar(230)
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.get_saldo()))
print("limite da conta corrente: R${:.2f}".format(conta_corrente.get_limite()))
resultado_2 = f"Saldo da conta corrente: R${conta_corrente.get_saldo():.2f}\nLimite da conta corrente: R${conta_corrente.get_limite():.2f}\n"

# Teste 3: fazer um saque e usar o limite na conta corrente
print("------------------------------------------------------\n")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
print("Teste 3: fazer um saque e usar o limite")
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.get_saldo()))
print("Saque de R$ 1200")
conta_corrente.sacar(1200)
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.get_saldo()))
resultado_3 = f"Saldo da conta corrente: R${conta_corrente.get_saldo():.2f}\nLimite da conta corrente: R${conta_corrente.get_limite():.2f}\n"


# Teste 4: fazer um saque e ultrapassar o limite na conta corrente
print("------------------------------------------------------\n")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
print("Teste 4: fazer um saque e ultrapassar o limite")
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.get_saldo()))
print("Saque de R$ 1800")
conta_corrente.sacar(1800)
resultado_4 = f"Saldo da conta corrente: R${conta_corrente.get_saldo():.2f}\nLimite da conta corrente: R${conta_corrente.get_limite():.2f}\n"

# Teste 5: fazer um depósito e verificar o saldo na conta corrente
print("------------------------------------------------------\n")
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)
print("Teste 5: fazer um depósito e verificar o saldo")
print("Saldo da conta corrente: R${:.2f}".format(conta_corrente.get_saldo()))
print("Depósito de R$ 2500")
conta_corrente.depositar(2500)
print("Saldo da conta corrente: R${:.2f}".format(
    conta_corrente.get_saldo() + conta_corrente.get_limite()))
resultado_5 = f"Saldo da conta corrente: R${conta_corrente.get_saldo():.2f}\nLimite da conta corrente: R${conta_corrente.get_limite():.2f}\n"

# Teste 6: verificar saldo da conta poupança e a taxa de rendimento
print("------------------------------------------------------\n")
print("Teste 6: verificar saldo da conta poupança e a taxa de rendimento")
conta_poupanca = ContaPoupanca(
    id_conta=2, saldo=100000000, taxa_de_rendimento=5)

print("Saldo da conta poupança: R${:.2f}".format(conta_poupanca.get_saldo()))
print("Rendimento da conta poupança por segundo: R${:.2f}".format(
    conta_poupanca.get_rendimento_por_periodo("segundos")))
print("Rendimento da conta poupança por minuto: R${:.2f}".format(
    conta_poupanca.get_rendimento_por_periodo("minutos")))
print("Rendimento da conta poupança por hora: R${:.2f}".format(
    conta_poupanca.get_rendimento_por_periodo("horas")))
print("Rendimento da conta poupança por dia: R${:.2f}".format(
    conta_poupanca.get_rendimento_por_periodo("dias")))
print("Rendimento da conta poupança por mês: R${:.2f}".format(
    conta_poupanca.get_rendimento_por_periodo("meses")))
print("Rendimento da conta poupança por ano: R${:.2f}".format(
    conta_poupanca.get_rendimento_por_periodo("anos")))
resultado_6 = f"Saldo da conta poupança: R${conta_poupanca.get_saldo():.2f}\n" \
    f"Rendimento da conta poupança por segundo: R${conta_poupanca.get_rendimento_por_periodo('segundos'):.2f}\n" \
    f"Rendimento da conta poupança por minuto: R${conta_poupanca.get_rendimento_por_periodo('minutos'):.2f}\n" \
    f"Rendimento da conta poupança por hora: R${conta_poupanca.get_rendimento_por_periodo('horas'):.2f}\n" \
    f"Rendimento da conta poupança por dia: R${conta_poupanca.get_rendimento_por_periodo('dias'):.2f}\n" \
    f"Rendimento da conta poupança por mês: R${conta_poupanca.get_rendimento_por_periodo('meses'):.2f}\n" \
    f"Rendimento da conta poupança por ano: R${conta_poupanca.get_rendimento_por_periodo('anos'):.2f}\n"


# Teste 7: fazer um saque e verificar o saldo na conta poupança
print("------------------------------------------------------\n")
print("Teste 7: fazer um saque da conta poupança e verificar o saldo")
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=10)
print("Saldo da conta poupança: R${:.2f}".format(conta_poupanca.get_saldo()))
print("Valor do saque: R$500")
conta_poupanca.sacar(500)
conta_poupanca.get_saldo()
resultado_7 = f"Saldo da conta poupança: R${conta_poupanca.get_saldo():.2f}\n"

# Teste 8: fazer um depósito e verificar o saldo na conta poupança
print("------------------------------------------------------\n")
print("Teste 8: fazer um depósito e verificar o saldo da conta poupança")
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=10)
print("Saldo da conta poupança: R${:.2f}".format(conta_poupanca.get_saldo()))
print("Valor do depósito: R$2500")
conta_poupanca.depositar(2500)
conta_poupanca.get_saldo()
resultado_8 = f"Saldo da conta poupança: R${conta_poupanca.get_saldo():.2f}\n"

# Teste 9: fazer um saque e ultrapassar o saldo na conta poupança
print("------------------------------------------------------\n")
print("Teste 9: fazer um saque e ultrapassar o saldo da conta poupança")
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=10)
print("Saldo da conta poupança: R${:.2f}".format(conta_poupanca.get_saldo()))
print("Valor do saque: R$6000")
conta_poupanca.sacar(6000)
resultado_9 = f"Saldo da conta poupança: R${conta_poupanca.get_saldo():.2f}\n"


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
