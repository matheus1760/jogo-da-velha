# Biblioteca necessária para uso da função sleep()
import time

# Importação da classe "Jogador"
from jogador import Jogador


# Método com um array como argumento para mostrar o tabuleiro
# Note o uso da type hint, que é uma "dica" para outros programadores
def tabuleiro(elemento: list) -> None:
    print()
    # Este estilo de formatação é mais compacto que o usual
    print(f"{elemento[0]} | {elemento[1]} | {elemento[2]}")
    print(f"{elemento[3]} | {elemento[4]} | {elemento[5]}")
    print(f"{elemento[6]} | {elemento[7]} | {elemento[8]}")


print("Bem vindo à Jogo da Velha! pressione ENTER para começar:")
# O input() por si espera um uma confirmação de um dispositivo de entrada
input()

print("Carregando...")
# O sistema fica ocioso por 3 segundos
time.sleep(3)

# Criação dos dos objetos sem nome, para depois nomeá-los com consdições
jogador1 = Jogador("", 1, "0")
jogador1.nomear_jogador()
jogador2 = Jogador("", 2, "x")
jogador2.nomear_jogador()


while True:
    if jogador2.nome == jogador1.nome:
        print("Jogador 2, seu nome é igual ao jogador 1. Escolha outro nome!")
        jogador2.nomear_jogador()
    break

# Também é possível utilizar o "\n" no começo do print para quebrar a linha
print("\nComo jogar:")
print("Cada casa do jogo da velha tem um número associado.")
print("Veja a ilustração:")

tabuleiro([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("\nPara ganhar, você precisa conseguir 3 em linha,")
print("na horizontal, na vertical ou na diagonal.\n")

time.sleep(5)

print(f"{jogador1.nome}(bolinha) vs {jogador2.nome}(x)!")


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


def checar_empate(elemento: list) -> bool:
    for i in range(9):

        if elemento[i] == " ":
            return False

    return True


def rodada(elemento: list, num_rodada) -> None:
    if num_rodada % 2 == 0:
        nome_jogador = jogador2.nome
        símbolo = jogador2.símbolo
    else:
        nome_jogador = jogador1.nome
        símbolo = jogador1.símbolo

    # Note que é possível utilizar métodos dentro de métodos
    tabuleiro(elemento)

    print(f"Rodada {num_rodada}!")
    print(f"{nome_jogador}, digite o número da casa que deseja jogar:")

    jogada = int(input())

    # É usado o range(1, 10) e não o range(9), pois o tabuleiro começa em 0
    if jogada in range(1, 10):

        # O -1 é usado, pois o range começa em 1, e o array começa em 0.
        if elemento[jogada - 1] == " ":
            elemento[jogada - 1] = símbolo
        else:
            print("Casa ocupada, escolha outra")
            rodada(elemento, num_rodada)

    else:
        print("Jogada inválida, escolha outra")
        rodada(elemento, num_rodada)


# Tabuleiro inicial
elemento = [" "] * 9
num_rodada = 1

# Comportamento geral do jogo
while True:

    rodada(elemento, num_rodada)

    if checar_vitoria(elemento) is True:
        tabuleiro(elemento)

        if num_rodada % 2 != 0:
            print(f"{jogador1.nome}, jogador ({jogador1.número}) ganhou!")
        else:
            print(f"{jogador2.nome}, jogador({jogador2.número}) ganhou!")

        print(f"Você venceu na {num_rodada}ª rodada!")
        break

    if checar_empate(elemento) is True:
        tabuleiro(elemento)
        print("Empate!")
        break

    num_rodada += 1

    time.sleep(0.5)
