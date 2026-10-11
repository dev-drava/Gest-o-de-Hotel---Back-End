class Quarto(git ):
    def __init__(self, numero, tipo, preco_diaria):
        self._numero = numero
        self._tipo = tipo
        self._preco_diaria = preco_diaria

    @property
    def numero(self):
        return self._numero

    @property
    def tipo(self):
        return self._tipo

    @property
    def preco_diaria(self):
        return self._preco_diaria

    @abstractmethod
    def mostrar_informacoes(self):
        pass

