from Conta_Poupanca import ContaPoupanca
from menu_valor_simulacao_rendimento import selecionar_opcao_simulacao_rendimento

# Cria uma conta poupança com saldo 5000 e taxa de rendimento 15%
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=15)


def consultar_saldo_conta_poupanca() -> None:

    print("\nSaldo atual: R${:.2f}".format(conta_poupanca._saldo))


def realizar_saque_conta_poupanca() -> None:
    continuar_loop = True
    while continuar_loop:
        valor_saque = input("Digite o valor do saque: R$")
        if valor_saque.isnumeric():
            conta_poupanca.sacar(valor=float(valor_saque))
            continuar_loop = False
        else:
            print("Valor inválido. Digite apenas números.\n")


def realizar_deposito_conta_poupanca() -> None:
    continuar_loop = True
    while continuar_loop:
        valor_deposito = input("Digite o valor do depósito: R$")
        if valor_deposito.isnumeric():
            conta_poupanca.depositar(valor=float(valor_deposito))
            continuar_loop = False
        else:
            print("Valor inválido. Digite apenas números.\n")


def verificar_rendimento_conta_poupanca() -> None:

    # mostrar o saldo atual da conta poupança
    print("\nSaldo atual: R${:.2f}".format(conta_poupanca._saldo))

    print("\nRendimento por período:")
    rendimento_por_segundo = conta_poupanca.calcular_rendimento_por_segundo()
    rendimento_por_minuto = conta_poupanca.calcular_rendimento_por_minuto()
    rendimento_por_hora = conta_poupanca.calcular_rendimento_por_hora()
    rendimento_por_dia = conta_poupanca.calcular_rendimento_por_dia()
    rendimento_por_mes = conta_poupanca.calcular_rendimento_por_mes()
    rendimento_por_ano = conta_poupanca.calcular_rendimento_por_ano()

    print("Rendimento por segundo: R${:.2f}".format(rendimento_por_segundo))
    print("Rendimento por minuto: R${:.2f}".format(rendimento_por_minuto))
    print("Rendimento por hora: R${:.2f}".format(rendimento_por_hora))
    print("Rendimento por dia: R${:.2f}".format(rendimento_por_dia))
    print("Rendimento por mês: R${:.2f}".format(rendimento_por_mes))
    print("Rendimento por ano: R${:.2f}".format(rendimento_por_ano))

    selecionar_opcao_simulacao_rendimento()


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
