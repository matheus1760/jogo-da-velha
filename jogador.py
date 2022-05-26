class Jogador:
    def __init__(self, nome, número, símbolo: str):
        self.__nome = nome
        self.__número = número
        self.__símbolo = símbolo

    @property
    def nome(self):
        # O método title() deixa a primeira letra maiúscula
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def símbolo(self):
        return self.__símbolo.title()

    @property
    def número(self):
        return self.__número

    # Se o nome for uma string não nula, o argumento será o novo nome do objeto
    def nomear_jogador(self) -> None:
        print(f"Digite o nome do jogador {self.número}:")
        while True:
            nome = input()
            print()

            if nome == "":
                print("Nome inválido, tente novamente")          
            else:
                self.nome = nome
                break
