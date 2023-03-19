import random
from personagem import Personagem
from monstro import Lobo, Goblin


def batalha(personagem, monstro):
    nome_personagem = personagem.nome if isinstance(
        personagem, Personagem) else personagem.tipo
    nome_monstro = monstro.nome if isinstance(
        monstro, Personagem) else monstro.tipo
    print(f'{nome_personagem} está batalhando contra um {nome_monstro}!')
    print(f'{nome_personagem} tem {personagem.pontos_vida} pontos de vida')
    print(f'{nome_monstro} tem {monstro.pontos_vida} pontos de vida')

    while personagem.pontos_vida > 0 and monstro.pontos_vida > 0:
        ataque_personagem = random.randint(1, personagem.pontos_ataque)
        ataque_monstro = random.randint(1, monstro.pontos_ataque)

        print(f'{nome_personagem} atacou o {nome_monstro} e causou {ataque_personagem} {"ponto" if ataque_personagem == 1 else "pontos"} de dano.')

        if monstro.pontos_vida <= 0:
            print(f'O {nome_monstro} foi derrotado!')
            break

        print(f'{nome_monstro} atacou {nome_personagem} e causou {ataque_monstro} {"ponto" if ataque_monstro == 1 else "pontos"} de dano.')

        personagem.pontos_vida -= ataque_monstro

        if personagem.pontos_vida <= 0:
            print(f'{nome_personagem} foi derrotado!')
            break

        print(f'{nome_personagem}: {personagem.pontos_vida} {"ponto" if personagem.pontos_vida == 1 else "pontos"} de vida')
        print(f'{nome_monstro}: {monstro.pontos_vida} {"ponto" if monstro.pontos_vida == 1 else "pontos"} de vida')


# Instanciando os personagens e monstros com valores aleatórios
personagem = Personagem('João', random.randint(10, 20), random.randint(1, 5))
lobo = Lobo(random.randint(5, 15), random.randint(1, 4), random.randint(1, 10))
goblin = Goblin(random.randint(1, 5), random.randint(1, 10))

# Criando uma lista com os personagens e monstros
personagens_e_monstros = [personagem, lobo, goblin]

# Escolhendo aleatoriamente dois personagens e/ou monstros diferentes da lista
personagem_1, personagem_2 = random.sample(personagens_e_monstros, k=2)

# Chamando a função batalha com os dois personagens e/ou monstros escolhidos
batalha(personagem_1, personagem_2)
