from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca


# Criar uma conta corrente com um saldo de R$1000,00 e um limite de R$500,00
conta_corrente = ContaCorrente(id_conta=1, saldo=1000, limite=500)

# Criar uma conta poupança com um saldo de R$5000,00 e uma taxa de rendimento de 2% ao mês
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=2)


def selecionar_conta() -> None:
    """
    Função que permite selecionar uma conta (corrente ou poupança) e executar suas respectivas operações.
    """
    opcoes_conta = ["1", "2", "3"]
    opcao_conta = ""

    while opcao_conta != "3":
        print("\nSelecione uma opção de conta:")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")
        print("3 - Sair")

        opcao_conta = input("Digite a opção selecionada: ")

        if opcao_conta not in opcoes_conta:
            print("Opção inválida.")
            continue

        if opcao_conta == "1":
            selecionar_opcao_conta_corrente()
        elif opcao_conta == "2":
            selecionar_opcao_conta_poupanca()
        else:
            break


def selecionar_opcao_conta_corrente() -> None:
    """
    Função que permite selecionar uma operação a ser realizada na conta corrente.
    """
    opcao_conta_corrente = ["1", "2", "3", "4"]
    opcao_conta_corrente = ""

    while opcao_conta_corrente != "4":
        print("\nConta Corrente selecionada")
        print("Selecione uma opção:")
        print("1 - Consultar saldo de conta corrente")
        print("2 - Realizar saque em conta corrente")
        print("3 - Realizar depósito em conta corrente")
        print("4 - Voltar")

        opcao_conta_corrente = input("Digite a opção selecionada: ")

        if opcao_conta_corrente not in opcao_conta_corrente:
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


def selecionar_opcao_conta_poupanca() -> None:
    """
    Função que permite selecionar uma operação a ser realizada na conta poupança.
    """
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
    """
    Função que imprime o saldo da conta poupança.
    """
    print("\nSaldo atual: R${:.2f}".format(conta_poupanca.get_saldo()))


def realizar_saque_conta_poupanca() -> None:
    """
    Função que realiza um saque na conta poupança.
    """
    valor_saque = float(input("Digite o valor do saque: R$").replace(",", "."))
    conta_poupanca.sacar(valor=valor_saque)


def realizar_deposito_conta_poupanca() -> None:
    """
    Função que realiza um depósito na conta poupança.
    """
    valor_deposito = float(
        input("Digite o valor do depósito: R$").replace(",", "."))

    conta_poupanca.depositar(valor=valor_deposito)


def verificar_rendimento_conta_poupanca() -> None:
    """
    Função que imprime o rendimento da conta poupança.
    """

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
        conta_poupanca.get_rendimento_por_periodo('ano')))


selecionar_conta()
