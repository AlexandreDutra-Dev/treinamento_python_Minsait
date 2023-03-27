from ContaCorrente import ContaCorrente

# Criar uma conta corrente com um saldo de R$1000,00 e um limite de R$500,00
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)


def selecionar_opcao_conta_corrente() -> None:
    """
    Função que permite selecionar uma operação a ser realizada na conta corrente.
    """
    opcoes_conta_corrente = ["1", "2", "3", "4"]
    opcao_conta_corrente = ""

    while opcao_conta_corrente != "4":
        print("\nConta Corrente selecionada")
        print("Selecione uma opção:")
        print("1 - Consultar saldo de conta corrente")
        print("2 - Realizar saque em conta corrente")
        print("3 - Realizar depósito em conta corrente")
        print("4 - Voltar")

        opcao_conta_corrente = input("Digite a opção selecionada: ")

        if opcao_conta_corrente not in opcoes_conta_corrente:
            print("Opção inválida.")
            continue

        if opcao_conta_corrente == "1":
            consultar_saldo_conta_corrente()
        elif opcao_conta_corrente == "2":
            realizar_saque_conta_corrente()
        elif opcao_conta_corrente == "3":
            realizar_deposito_conta_corrente()
        else:
            break


def consultar_saldo_conta_corrente() -> None:
    """
    Função que imprime o saldo da conta corrente e o limite disponível.
    """
    print("\nSaldo atual: R${:.2f}".format(conta_corrente.get_saldo()))
    print("Limite disponível: R${:.2f}".format(conta_corrente.get_limite()))
    print("Saldo total: R${:.2f}".format(
        conta_corrente.get_saldo() + conta_corrente.get_limite()))


def realizar_saque_conta_corrente() -> None:
    """
    Função que realiza um saque na conta corrente.
    """
    valor_saque = float(input("Digite o valor do saque: R$").replace(",", "."))
    conta_corrente.sacar(valor=valor_saque)


def realizar_deposito_conta_corrente() -> None:
    """
    Função que realiza um depósito na conta corrente.
    """
    valor_deposito = float(
        input("Digite o valor do depósito: R$").replace(",", "."))
    conta_corrente.depositar(valor=valor_deposito)
