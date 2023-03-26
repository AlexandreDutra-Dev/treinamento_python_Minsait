from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Criar uma conta corrente com um saldo de R$1000,00 e um limite de R$500,00
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)

# Criar uma conta poupança com um saldo de R$5000,00 e uma taxa de rendimento de 2%
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=2)


# Loop para transações
while True:
    print("\nSelecione uma opção:")
    print("1 - Realizar saque em conta corrente")
    print("2 - Realizar depósito em conta corrente")
    print("3 - Realizar saque em conta poupança")
    print("4 - Realizar depósito em conta poupança")
    print("5 - Realizar depósito em conta comum")
    print("6 - Consulta de saldo:")
    print("7 - Sair")

    opcao = input("Digite a opção selecionada: ")

    if opcao == "1":
        # Realizar saque em conta corrente
        valor = float(input("Digite o valor do saque: "))
        try:
            conta_corrente.sacar(valor)
            print(
                f"Saque realizado com sucesso. Saldo atual: {conta_corrente.get_saldo()}")
        except ValueError as e:
            print(f"Erro ao realizar saque: {str(e)}")

    elif opcao == "2":
        # Realizar depósito em conta corrente
        valor = float(input("Digite o valor do depósito: "))
        conta_corrente.depositar(valor)
        print(
            f"Depósito realizado com sucesso. Saldo atual: {conta_corrente.get_saldo()}")

    elif opcao == "3":
        # Realizar saque em conta poupança
        valor = float(input("Digite o valor do saque: "))
        try:
            conta_poupanca.sacar(valor)
            print(
                f"Saque realizado com sucesso. Saldo atual: {conta_poupanca.get_saldo()}")
        except ValueError as e:
            print(f"Erro ao realizar saque: {str(e)}")

    elif opcao == "4":
        # Realizar depósito em conta poupança
        valor = float(input("Digite o valor do depósito: "))
        conta_poupanca.depositar(valor)
        print(
            f"Depósito realizado com sucesso. Saldo atual: {conta_poupanca.get_saldo()}")

    elif opcao == "5":
       # Consulta de saldo
        print("Selecione uma opção:")
        print("1 - Consultar saldo da conta corrente")
        print("2 - Consultar saldo da conta poupança")
        print("3 - Consultar saldo da conta comum")

        opcao = input("Digite a opção selecionada: ")

        if opcao == "1":
            print(f"Saldo da conta corrente: {conta_corrente.get_saldo()}")
        elif opcao == "2":
            print(f"Saldo da conta poupança: {conta_poupanca.get_saldo()}")
        else:
            print("Opção inválida.")

    elif opcao == "6":
        # Sair
        print("Saindo do sistema...")
        break
