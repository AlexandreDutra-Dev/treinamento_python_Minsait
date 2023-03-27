from Conta_Poupanca import ContaPoupanca

# Cria uma conta poupança com saldo 5000 e taxa de rendimento 15%
conta_poupanca = ContaPoupanca(id_conta=2, saldo=5000, taxa_de_rendimento=15)


def selecionar_opcao_simulacao_rendimento() -> None:

    opcoes_simulacao = ["1", "2"]
    opcao_simulacao = ""

    while opcao_simulacao != "2":
        print("\nDeseja fazer uma simulação de rendimento?")
        print("1 - Sim")
        print("2 - Não")

        opcao_simulacao = input("Digite a opção selecionada: ")

        if opcao_simulacao not in opcoes_simulacao:
            print("Opção inválida.")
            continue

        if opcao_simulacao == "1":
            valor_simulacao = float(
                input("Digite o valor que deseja simular: R$").replace(",", "."))
            print("\nRendimento por período:")
            print("Por segundos: R${:.2f}".format(
                conta_poupanca.get_rendimento_por_periodo('segundos', valor_simulacao)))
            print("Por minutos: R${:.2f}".format(
                conta_poupanca.get_rendimento_por_periodo('minutos', valor_simulacao)))
            print("Por horas: R${:.2f}".format(
                conta_poupanca.get_rendimento_por_periodo('horas', valor_simulacao)))
            print("Por dias: R${:.2f}".format(
                conta_poupanca.get_rendimento_por_periodo('dias', valor_simulacao)))
            print("Por meses: R${:.2f}".format(
                conta_poupanca.get_rendimento_por_periodo('meses', valor_simulacao)))
            print("Por anos: R${:.2f}".format(
                conta_poupanca.get_rendimento_por_periodo('anos', valor_simulacao)))
        else:
            break
