from Monstro import Monstro


class Lobo(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, força):
        super().__init__('Lobo', pontos_vida, pontos_ataque)
        self.força = força
