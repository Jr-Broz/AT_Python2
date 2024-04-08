import random
from perguntas import *

perguntas_utilizadas = set()

def randomizar_pergunta():
    pergunta = {
        1: pergunta_um, 
        2: pergunta_dois,
        3: pergunta_tres,
        4: pergunta_quatro,
        5: pergunta_cinco,
        6: pergunta_seis,
        7: pergunta_sete,
        8: pergunta_oito,
        9: pergunta_nove,
        10: pergunta_dez,
        11: pergunta_onze,
        12: pergunta_doze,
        13: pergunta_treze,
        14: pergunta_quatorze,
        15: pergunta_quinze
    }

    quantidade_acertos = 0
    quantidade_erros = 0

    while quantidade_acertos < 5 and quantidade_erros < 5:
        escolha_aleatoria = random.randint(1, 15)
        
        if escolha_aleatoria not in perguntas_utilizadas:
            perguntas_utilizadas.add(escolha_aleatoria)

            pergunta_escolhida = pergunta[escolha_aleatoria]
            resposta = pergunta_escolhida()

            if resposta:
                quantidade_acertos += 1
            else:
                quantidade_erros += 1

    if quantidade_acertos == 5:
        print("Você chegou ao final do jogo! Parabéns!")
    else:
        print("Você perdeu. Obrigado por jogar.")

    resposta = input("Quer jogar novamente? (1 - Sim, 2 - Não): ")
    if resposta == '1':
        perguntas_utilizadas.clear()
        randomizar_pergunta()
    else:
        print("Ok, obrigado por jogar.")

randomizar_pergunta()
