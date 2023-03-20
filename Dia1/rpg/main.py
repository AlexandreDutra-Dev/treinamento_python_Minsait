import random
from personagem import Personagem
from lobo import Lobo
from goblin import Goblin

# Função para iniciar a batalha entre um personagem e um monstro
def batalha(personagem, monstro):
    nome_personagem = personagem.nome if isinstance(
        personagem, Personagem) else personagem.tipo
    nome_monstro = monstro.nome if isinstance(
        monstro, Personagem) else monstro.tipo

    # Verifica se o monstro é do tipo Lobo ou Goblin
    if isinstance(monstro, (Lobo, Goblin)):
        print('Inicio da batalha')
        print('----------')
        print(f'{nome_monstro} está batalhando contra o {nome_personagem}!')
    else:
        print(f'{nome_personagem} está batalhando contra o {nome_monstro}!')

    # Mostra a quantidade de pontos de vida dos dois
    print(f'{nome_monstro} tem {monstro.pontos_vida} pontos de vida.')
    print(f'{nome_personagem} tem {personagem.pontos_vida} pontos de vida.\n')

    # Enquanto os dois tiverem pontos de vida, a batalha continua
    while personagem.pontos_vida > 0 and monstro.pontos_vida > 0:
        ataque_personagem = random.randint(1, personagem.pontos_ataque)
        ataque_monstro = random.randint(1, monstro.pontos_ataque)

        print(
            f'{nome_personagem} atacou o {nome_monstro} e causou {ataque_personagem} ponto(s) de dano.')
        monstro.pontos_vida -= ataque_personagem

        # Verifica se o monstro morreu
        if monstro.pontos_vida <= 0:
            nome_vencedor = nome_personagem
            nome_perdedor = nome_monstro
            pontos_vida_vencedor = personagem.pontos_vida

            print('')

            print(
                f'Fim da batalha:\n---------------\n{nome_vencedor} venceu a batalha com {pontos_vida_vencedor} pontos de vida restantes!')
            print(f'{nome_perdedor} foi derrotado.')
            break

        # Mostra a quantidade de pontos de vida restantes do monstro
        print(f'{nome_monstro} tem {monstro.pontos_vida} pontos de vida restantes.\n')

        print(
            f'{nome_monstro} atacou {nome_personagem} e causou {ataque_monstro} ponto(s) de dano.')
        personagem.pontos_vida -= ataque_monstro

        # Verifica se o humano morreu
        if personagem.pontos_vida <= 0:
            print(f'{nome_personagem} foi derrotado!')
            break

        # Mostra a quantidade de pontos de vida restantes do humano e do monstro
        print(f'{nome_personagem} tem {personagem.pontos_vida} ponto(s) de vida')
        print(f'{nome_monstro} tem {monstro.pontos_vida} ponto(s) de vida\n')


# Instanciando os personagens e monstros com valores aleatórios
humano = Personagem('João', random.randint(10, 20), random.randint(1, 5))
lobo = Lobo(random.randint(5, 15), random.randint(1, 4))
goblin = Goblin(random.randint(1, 5), random.randint(
    1, 10))

# Criando uma lista com os personagens e monstros
personagens_e_monstros = [humano, lobo, goblin]

# Escolhendo aleatoriamente dois personagens e/ou monstros diferentes da lista
personagem_1, personagem_2 = random.sample(personagens_e_monstros, k=2)

# Chamando a função batalha com os dois personagens e/ou monstros escolhidos
batalha(personagem_1, personagem_2)
