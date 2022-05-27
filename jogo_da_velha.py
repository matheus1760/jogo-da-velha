# Biblioteca necessária para uso da função sleep()
import time


# Método com um array como argumento para mostrar o tabuleiro
def tabuleiro(elemento: list) -> None:
    print()
    print(f"{elemento[0]} | {elemento[1]} | {elemento[2]}")
    print(f"{elemento[3]} | {elemento[4]} | {elemento[5]}")
    print(f"{elemento[6]} | {elemento[7]} | {elemento[8]}")


print("Bem vindo à Jogo da Velha! pressione ENTER para começar:")
# O input() por si espera um uma confirmação de um dispositivo de entrada

print("\nCarregando...")
# O sistema fica ocioso por 3 segundos
time.sleep(3)
# O print() por si apenas imprime uma nova linha

print("\nJogador 1(bolinha), digite seu nome:\n")
jogador1 = input().title()

print("\nJogador 2(xis), digite seu nome:\n")
jogador2 = input().title()

print("\nComo jogar:")
print("Cada casa do jogo da velha tem um número associado.")
print("Veja a ilustração:")

tabuleiro([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("\nPara ganhar, você precisa conseguir 3 em linha,")
print("na horizontal, na vertical ou na diagonal.\n")

time.sleep(5)

print(f"{jogador1}(bolinha) vs {jogador2}(x)!")


def checar_vitoria(elemento: list) -> bool:
    for i in range(3):

        # Se a casa 1, 2 e 3 estão com o mesmo símbolo, alguém ganhou
        # Vitória na horizontal
        if elemento[i] == elemento[i + 1] == elemento[i + 2] != " ":
            return True

        # Vitória na vertical
        if elemento[i] == elemento[i + 3] == elemento[i + 6] != " ":
            return True

        # Vitórias na diagonal
        if elemento[0] == elemento[4] == elemento[8] != " ":
            return True
        if elemento[2] == elemento[4] == elemento[6] != " ":
            return True

    # Se o return False não está identado, não precisa do else
    return False


def rodada(elemento: list, num_jogador, num_rodada, jogador: str) -> None:
    if num_jogador == 1:
        simbolo = "O"
    else:
        simbolo = "X"

    # Note que é possível utilizar métodos dentro de métodos
    tabuleiro(elemento)

    print("Rodada {}!".format(num_rodada))
    print(f"{jogador}, digite o número da casa que deseja jogar:")

    jogada = int(input())

    # É usado o range(1, 10) e não o range(9), pois o tabuleiro começa em 0
    if jogada in range(1, 10):

        # O -1 é usado, pois o range começa em 1, e o array começa em 0.
        if elemento[jogada - 1] == " ":
            elemento[jogada - 1] = simbolo
        else:
            print("Casa ocupada, escolha outra")

            rodada(elemento, num_jogador, num_rodada, jogador)

    else:
        print("Jogada inválida, escolha outra")
        rodada(elemento, num_jogador, num_rodada, jogador)


elemento = [" "] * 9
num_rodada = 1
# Se o contador for par, é a vez do jogador 1, senão, é a vez do jogador 2
contador_jogador = 0

while True:
    if contador_jogador % 2 == 0:
        jogador = jogador1
        num_jogador = 1
    else:
        jogador = jogador2
        num_jogador = 2

    rodada(elemento, num_jogador, num_rodada, jogador)

    if checar_vitoria(elemento) is True:

        tabuleiro(elemento)

        print(f"{jogador} venceu!, Parabéns")
        print(f"Você venceu na {num_rodada}ª rodada!")
        break

    num_rodada += 1
    contador_jogador += 1

    time.sleep(0.5)
