from Conta_Poupanca import ContaPoupanca
from menu_valor_simulacao_rendimento import selecionar_opcao_simulacao_rendimento

# Cria uma conta poupança com saldo 5000 e taxa de rendimento 15%
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=15)


def selecionar_opcao_conta_poupanca() -> None:

    opcoes_conta_poupanca = ["1", "2", "3", "4", "5"]
    opcao_conta_poupanca = ""

    while opcao_conta_poupanca != "5":
        print("\nConta Poupança selecionada")
        print("Selecione uma opção:")
        print("1 - Consultar saldo de conta poupança")
        print("2 - Realizar saque em conta poupança")
        print("3 - Realizar depósito em conta poupança")
        print("4 - Verificar rendimento da conta poupança")
        print("5 - Voltar")

        opcao_conta_poupanca = input("Digite a opção selecionada: ")

        if opcao_conta_poupanca not in opcoes_conta_poupanca:
            print("Opção inválida.")
            continue

        if opcao_conta_poupanca == "1":
            consultar_saldo_conta_poupanca()
        elif opcao_conta_poupanca == "2":
            realizar_saque_conta_poupanca()
        elif opcao_conta_poupanca == "3":
            realizar_deposito_conta_poupanca()
        elif opcao_conta_poupanca == "4":
            verificar_rendimento_conta_poupanca()
        else:
            break


def consultar_saldo_conta_poupanca() -> None:

    print("\nSaldo atual: R${:.2f}".format(conta_poupanca.get_saldo()))


def realizar_saque_conta_poupanca() -> None:

    valor_saque = float(input("Digite o valor do saque: R$").replace(",", "."))
    conta_poupanca.sacar(valor=valor_saque)


def realizar_deposito_conta_poupanca() -> None:

    valor_deposito = float(
        input("Digite o valor do depósito: R$").replace(",", "."))

    conta_poupanca.depositar(valor=valor_deposito)


def verificar_rendimento_conta_poupanca() -> None:

    # mostrar o saldo atual da conta poupança
    print("\nSaldo atual: R${:.2f}".format(conta_poupanca.get_saldo()))

    print("\nRendimento por período:")
    print("Por segundos: R${:.2f}".format(
        conta_poupanca.get_rendimento_por_periodo('segundos')))
    print("Por minutos: R${:.2f}".format(
        conta_poupanca.get_rendimento_por_periodo('minutos')))
    print("Por horas: R${:.2f}".format(
        conta_poupanca.get_rendimento_por_periodo('horas')))
    print("Por dias: R${:.2f}".format(
        conta_poupanca.get_rendimento_por_periodo('dias')))
    print("Por meses: R${:.2f}".format(
        conta_poupanca.get_rendimento_por_periodo('meses')))
    print("Por anos: R${:.2f}".format(
        conta_poupanca.get_rendimento_por_periodo('anos')))

    selecionar_opcao_simulacao_rendimento()
