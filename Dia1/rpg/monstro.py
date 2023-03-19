from ser_vivo import SerVivo


class Monstro(SerVivo):
    def __init__(self, tipo, pontos_vida, pontos_ataque):
        super().__init__(pontos_vida, pontos_ataque)
        self.tipo = tipo

class Lobo(Monstro):
    def __init__(self, pontos_vida, pontos_ataque):
        super().__init__('Lobo', pontos_vida, pontos_ataque)

class Goblin(Monstro):
    def __init__(self, pontos_vida, pontos_ataque):
        super().__init__('Goblin', pontos_vida, pontos_ataque)
