from monstro import Monstro


class Goblin(Monstro):
    def __init__(self, pontos_vida, pontos_ataque):
        super().__init__('Goblin', pontos_vida, pontos_ataque)
