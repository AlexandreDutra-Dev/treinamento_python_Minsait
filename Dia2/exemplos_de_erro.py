def atualizar_candidato(self, indice_candidato, chave, valor):
    try:
        self.candidatos[indice_candidato][chave] = valor
    except IndexError:
        print(f"O índice {indice_candidato} não existe.")
    except ZeroDivisionError:
        self.candidatos[indice_candidato][chave] = 0


try:
    print("Vou conseguir executar, mas a instrução seguinte vai gerar um erro.")
    print(10/0)
    print("Essa instrução não será executada.")
except ZeroDivisionError as e:
    print(e)
    print(10)
