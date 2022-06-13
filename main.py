"""Arquivo principal"""

import time
from ascii import apresentacao, finalizacao


def tabuleiro(elemento: list) -> None:
    """Método com uma lista de 'strings' como argumento
    para mostrar o tabuleiro"""
    print()
    print(f"{elemento[0]} | {elemento[1]} | {elemento[2]}")
    print(f"{elemento[3]} | {elemento[4]} | {elemento[5]}")
    print(f"{elemento[6]} | {elemento[7]} | {elemento[8]}")


print(apresentacao)
print("pressione ENTER para começar:")

input()

print("Carregando...")

time.sleep(1)


def nomear_jogador(simbolo: str, numero: int) -> str:
    """Checa se o nome do jogador é válido"""
    while True:
        print(f"\nJogador {numero}({simbolo}), digite seu nome:")
        nome_jogador = input().title()
        if nome_jogador != "":
            return nome_jogador

        print("Nome Inválido, digite novamente:")


jogador1 = nomear_jogador("Círculo", 1)
jogador2 = nomear_jogador("X", 2)

print("\nComo jogar:")
print("Cada casa do jogo da velha tem um número associado. Veja a ilustração:")

tabuleiro([numbers for numbers in range(1, 10)])

print("\nPara ganhar, é preciso 3 símbolos consecutivos.\n")

time.sleep(3)

print(f"{jogador1}(círculo) vs {jogador2}(x)!")


def checar_vitoria(elemento: list) -> bool:
    """Método que checa se há vitoria a partir de uma lista de 'strings'"""
    # Até 6 porque existem testes com i + 2
    for i in range(len(elemento) - 2):
        # Se a casa 1, 2 e 3 estão com o mesmo símbolo, alguém ganhou
        # Vitória na horizontal
        if (elemento[i] == elemento[i + 1] == elemento[i + 2] or elemento[i - 1] == elemento[i] == elemento[i + 1] or
                elemento[i - 2] == elemento[i - 1] == elemento[i]) and elemento[i] != " ":
            return True

    for i in range(len(elemento) - 6):
        # Vitória na vertical
        if (elemento[i] == elemento[i + 3] == elemento[i + 6] or elemento[i - 3] == elemento[i] == elemento[i + 3] or
                elemento[i - 6] == elemento[i - 3] == elemento[i]) and elemento[i] != " ":
            return True

    # Vitórias na diagonal
    if elemento[0] == elemento[4] == elemento[8] != " ":
        return True

    if elemento[2] == elemento[4] == elemento[6] != " ":
        return True

    return False


def checar_empate(elemento: list) -> bool:
    """Se existe um elemento em branco no tabuleiro, há um empate"""
    return " " not in elemento


def rodada(elemento: list, num_jogador: int, num_rodada, jogador: str) -> None:
    """Método "principal" que recebe inúmeros argumentos e
    implementa as outras funções"""
    simbolo = "O" if num_jogador == 1 else "X"

    tabuleiro(elemento)

    print(f"Rodada {num_rodada}! {jogador}, digite o número da casa que deseja jogar:")

    jogada = int(input())

    # É usado o range(1, 10) e não o range(9), pois o tabuleiro começa em 0
    if jogada in range(1, 10):

        # O -1 é usado, pois, o range começa em 1, e a lista começa em 0.
        if elemento[jogada - 1] == " ":
            elemento[jogada - 1] = simbolo
        else:
            print("Casa ocupada, escolha outra")

            rodada(elemento, num_jogador, num_rodada, jogador)

    else:
        print("Jogada inválida, escolha outra")

        rodada(elemento, num_jogador, num_rodada, jogador)


elemento_do_jogo = [" "] * 9
# Se o contador for par, é a vez do jogador 1, senão, é a vez do jogador 2
for num_rodada_atual in range(1, 10):
    contador_jogador = num_rodada_atual - 1

    # O operador not serve para inverter o valor entre 0 e 1,
    # ou seja, se o contador for par, o número do jogador é 1, e vice-versa
    num_jogador_atual = not (contador_jogador % 2)

    jogador_atual = jogador1 if num_jogador_atual == 1 else jogador2

    rodada(elemento_do_jogo, num_jogador_atual,
           num_rodada_atual, jogador_atual)

    if checar_vitoria(elemento_do_jogo):
        tabuleiro(elemento_do_jogo)

        print(f"{jogador_atual} venceu!, Parabéns você venceu na {num_rodada_atual}ª rodada!")

        time.sleep(2)
        break

    if checar_empate(elemento_do_jogo):
        print("Empate!")
        break

    time.sleep(0.5)

print(finalizacao)
print("Feito com Python 3.10")
print("Obrigado por jogar")
