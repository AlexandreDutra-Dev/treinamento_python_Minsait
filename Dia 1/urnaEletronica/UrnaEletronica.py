class UrnaEletronica:
    def __init__(self):
        self.candidatos = [
            {"nome_candidato": "Alexandre", "partido": "JJJ"},
            {"nome_candidato": "Bia", "partido": "PPP"}
        ]

    def exibir_candidatos(self):
        print("Candidatos")
        for candidato in self.candidatos:
            print("Nome candidato:", candidato["nome_candidato"])
            print("Partido:", candidato["partido"])

    def adicionar_candidato(self, nome_candidato, partido):
        novo_candidato = {"nome_candidato": nome_candidato, "partido": partido}
        self.candidatos.append(novo_candidato)

    def remover_ultimo_candidato(self):
        if self.candidatos:
            self.candidatos.pop()
        else:
            print("Não há candidatos para remover")

    def atualizar_candidato(self, indice_candidato, chave, valor):
        try:
            self.candidatos[indice_candidato][chave] = valor
        except IndexError:
            print(f"Índice de candidato inválido: {indice_candidato}")


urna = UrnaEletronica()

print('------------------')
urna.exibir_candidatos()
urna.adicionar_candidato("Pedro", "PPS")
print('------------------')
urna.exibir_candidatos()
urna.remover_ultimo_candidato()
print('------------------')
urna.exibir_candidatos()

print('------------------')
urna.atualizar_candidato(0, "nome_candidato", "Beatriz")
urna.atualizar_candidato(0, "partido", "BBB")
urna.exibir_candidatos()
