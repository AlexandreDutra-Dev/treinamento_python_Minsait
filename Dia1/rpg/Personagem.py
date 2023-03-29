from Ser_Vivo import SerVivo


class Personagem(SerVivo):
    def __init__(self, nome, pontos_vida, pontos_ataque):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome
