class Reserva:
    def __init__(self, hospede, quarto, dias):
        self._hospede = hospede
        self._quarto = quarto
        self._dias = dias


    @property
    def hospede(self):
        return self._hospede

    @property
    def quarto(self):
        return self._quarto

    @property
    def dias(self):
        return self._dias

    def calcular_total(self):
        return self._dias * self._quarto.preco_diaria

    def mostrar_informacoes(self):
        print(f"Reserva: {self._hospede.nome} - Quarto {self._quarto.numero} - "
              f"{self._dias} dias - Total: {self.calcular_total():.2f}€")