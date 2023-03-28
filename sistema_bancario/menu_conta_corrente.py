from Conta_Corrente import ContaCorrente

# Cria uma conta corrente com um saldo de R$1000,00 e um limite de R$500,00
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)


def consultar_saldo_conta_corrente() -> None:

    print("\nSaldo atual: R${:.2f}".format(conta_corrente._saldo))
    print("Saldo total: R${:.2f}".format(
        conta_corrente._saldo + conta_corrente.limite))


def realizar_saque_conta_corrente() -> None:
    continuar_loop = True
    while continuar_loop:
        valor_saque = input("Digite o valor do saque: R$")
        if valor_saque.isnumeric():
            conta_corrente.sacar(valor=float(valor_saque))
            continuar_loop = False
        else:
            print("Valor inválido. Digite apenas números.\n")


def realizar_deposito_conta_corrente() -> None:
    continuar_loop = True
    while continuar_loop:
        valor_deposito = input("Digite o valor do depósito: R$")
        if valor_deposito.isnumeric():
            conta_corrente.depositar(valor=float(valor_deposito))
            continuar_loop = False
        else:
            print("Valor inválido. Digite apenas números.\n")


def selecionar_opcao_conta_corrente() -> None:

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
