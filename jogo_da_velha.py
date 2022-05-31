"""Biblioteca necessária para uso da função sleep()"""
import time


def tabuleiro(elemento: list) -> None:
    """Método com uma lista de strings como argumento
    para mostrar o tabuleiro"""
    print()
    print(f"{elemento[0]} | {elemento[1]} | {elemento[2]}")
    print(f"{elemento[3]} | {elemento[4]} | {elemento[5]}")
    print(f"{elemento[6]} | {elemento[7]} | {elemento[8]}")


print("Bem vindo à Jogo da Velha! pressione ENTER para começar:")

# O input() por si espera um uma confirmação de um dispositivo de entrada
input()

print("Carregando...")
# O sistema fica ocioso por 3 segundos
time.sleep(3)
# O print() por si apenas imprime uma nova linha

# Enquanto o nome do jogador não for válido, o programa pede novamente
while True:
    print("\nJogador 1(círculo), digite seu nome:\n")
    jogador1 = input().title()
    if jogador1 == "":
        print("Nome Inválido, digite novamente:")
        continue

    break


while True:
    print("\nJogador 2(x), digite seu nome:\n")

    jogador2 = input().title()
    if jogador2 == "":
        print("Nome Inválido, digite novamente:")
        continue

    break

print("\nComo jogar:")
print("Cada casa do jogo da velha tem um número associado.")
print("Veja a ilustração:")

# Usa-se a função tabuleiro() para mostrar o tabuleiro de exemplo
tabuleiro([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("\nPara ganhar, é preciso 3 símbolos consecutivos.\n")

time.sleep(5)

# Este é um tipo de formatação chamado de f-string
print(f"{jogador1}(círculo) vs {jogador2}(x)!")


def checar_vitoria(elemento: list) -> bool:
    """Método que checa se há vitoria a partir de uma lista de strings"""
    for i in range(6):

        # Se a casa 1, 2 e 3 estão com o mesmo símbolo, alguém ganhou
        # Vitória na horizontal
        if elemento[i] == elemento[i + 1] == elemento[i + 2] != " ":
            return True

    for i in range(3):

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
    """Método que checa se há empate a partir de uma lista de strings"""
    for i in range(9):
        if elemento[i] == " ":
            return False

    return True


def rodada(elemento: list, num_jogador: int, num_rodada,
           jogador: str) -> None:
    """Método "principal" que recebe inúmeros argumentos e
    implementa as outras funções"""
    if num_jogador == 1:
        simbolo = "O"
    else:
        simbolo = "X"

    # Note que é possível utilizar métodos dentro de métodos
    tabuleiro(elemento)

    print(f"Rodada {num_rodada}!")
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


elemento_do_jogo = [" "] * 9
# Se o contador for par, é a vez do jogador 1, senão, é a vez do jogador 2
for num_rodada_atual in range(1, 10):
    contador_jogador = num_rodada_atual - 1

    # O operador not serve para inverter o valor entre 0 e 1,
    # ou seja, se o contador for par, o número do jogador é 1, e vice-versa
    num_jogador_atual = not contador_jogador % 2

    # Operador ternário do python. Com isso, é possível fazer um if statement
    # com apenas uma linha, sem repetir o "jogador_atual = "
    jogador_atual = jogador1 if num_jogador_atual == 1 else jogador2

    rodada(elemento_do_jogo, num_jogador_atual,
           num_rodada_atual, jogador_atual)

    if checar_vitoria(elemento_do_jogo) is True:

        tabuleiro(elemento_do_jogo)

        print(f"{jogador_atual} venceu!, Parabéns")
        print(f"Você venceu na {num_rodada_atual}ª rodada!")
        break

    if checar_empate(elemento_do_jogo) is True:
        print("Empate!")
        break

    time.sleep(0.5)
