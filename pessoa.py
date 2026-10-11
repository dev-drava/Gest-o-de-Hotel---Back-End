from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = 0
        self.idade = idade        # passa pelo setter

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self.idade
    

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade <= 0:      # só aceita se não for negativa
            self._idade = nova_idade

    @abstractmethod
    def mostrar_informacoes(self):
        pass

try:
    Pessoa("Ana", 20)
except TypeError:
    print("Certo: Pessoa é abstrata")
    