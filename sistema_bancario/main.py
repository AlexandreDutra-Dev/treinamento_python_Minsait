from menu_conta_corrente import selecionar_opcao_conta_corrente
from menu_conta_poupanca import selecionar_opcao_conta_poupanca

# ...

def selecionar_conta() -> None:
    """
    Função que permite selecionar uma conta (corrente ou poupança) e realizar uma operação.
    """

    opcoes_conta = ["1", "2", "3"]
    opcao_conta = ""

    while opcao_conta != "3":
        print("\nSelecione uma conta:")
        print("1 - Conta Corrente")
        print("2 - Conta Poupança")
        print("3 - Voltar")

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


selecionar_conta()
