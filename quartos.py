from abc import ABC, abstractmethod


class Quarto(ABC):
    def __init__(self, numero, tipo, preco_diaria):
        self._numero = numero
        self._tipo = tipo
        self._ocupado = False
        self._preco_diaria = 0
        self.preco_diaria = preco_diaria   # usa o setter

    @property
    def numero(self):
        return self._numero

    @property
    def tipo(self):
        return self._tipo

    @property
    def ocupado(self):
        return self._ocupado

    @property
    def preco_diaria(self):
        return self._preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, novo_preco):
        if novo_preco >= 0:            # não aceita preços negativos
            self._preco_diaria = novo_preco

    def ocupar(self):
        self._ocupado = True

    def liberar(self):
        self._ocupado = False

    @abstractmethod
    def descricao(self):
        pass

    def mostrar_informacoes(self):
        if self._ocupado:
            estado = "ocupado"
        else:
            estado = "livre"
        print(f"Quarto {self._numero} ({self._tipo}) - {self._preco_diaria:.2f}€ por diária - {estado}")


class QuartoSimples(Quarto):
    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "simples", preco_diaria)

    def descricao(self):
        return "Quarto simples"


class QuartoLuxo(Quarto):
    def __init__(self, numero, preco_diaria, servicos):
        super().__init__(numero, "luxo", preco_diaria)
        self._servicos = servicos          # uma lista, ex.: ["Spa", "Jacuzzi"]

    def descricao(self):
        return "Quarto de luxo com serviços incluídos"

    def mostrar_informacoes(self):
        super().mostrar_informacoes()      # mostra o que o Quarto já mostra
        for servico in self._servicos:     # e depois os serviços
            print(f"   - {servico}")