from ser_vivo import SerVivo


class Monstro(SerVivo):
    def __init__(self, tipo, pontos_vida, pontos_ataque):
        super().__init__(pontos_vida, pontos_ataque)
        self.tipo = tipo
