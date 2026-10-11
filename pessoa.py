from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = 0
        self.idade = idade          # usa o setter

    @property
    def nome(self):
<<<<<<< Updated upstream
        return seelf.nome
=======
        return self._nome
>>>>>>> Stashed changes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:         # não aceita idades negativas
            self._idade = nova_idade

    @abstractmethod
    def mostrar_informacoes(self):
        pass


if __name__ == "__main__":
    try:
        Pessoa("Ana", 20)
    except TypeError:
        print("Certo: Pessoa é abstrata")