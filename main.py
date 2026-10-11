from pessoa import Pessoa
from quartos import Quarto, QuartoSimples, QuartoLuxo
from hospedes import Hospede
from reserva import Reserva
from funcionarios import Gerente, Recepcionista
from tecnicos import TecnicoManutencao, TecnicoRecepcao

# teste - david
try:
    Pessoa("Teste", 20)
except TypeError:
    print("Pessoa é abstrata.")

try:
    Quarto(666, "teste", 10)
except TypeError:
    print("Quarto é abstrato.")


quartos = [
    QuartoSimples(42, 50),
    QuartoSimples(13, 50),
    QuartoLuxo(67, 120, ["Spa", "Pequeno-almoço"]),
    QuartoLuxo(68, 150, ["Spa", "Varanda"]),
]

quartos_por_numero = {}
for quarto in quartos:
    quartos_por_numero[quarto.numero] = quarto

print("\n Quartos ")
for quarto in quartos:
    quarto.mostrar_informacoes()

# funcionarios -hery
gerente = Gerente("Ana", 45, 2500)
rececionista = Recepcionista("Rui", 1, 30, 1200, "manhã")
tecnico = TecnicoManutencao("Paulo", 38, 1400, "eletricidade")
tecnico_rececao = TecnicoRecepcao("Marta", 2, 1500, "Receção", "canalização")

funcionarios = [gerente, rececionista, tecnico, tecnico_rececao]

print()
gerente.gerar_relatorio(funcionarios)

# hospede -david 
fila_de_espera = [
    Hospede("João", 69, 3),
    Hospede("Maria", 42, 5),
    Hospede("Carlos", 67, 2),
]
quartos_pedidos = (42, 67, 69)   # o carlos pediu um quarto já ocupado

lista_hospedes = []
posicao = 0
while posicao < len(fila_de_espera):
    hospede = fila_de_espera[posicao]
    rececionista.registrar_hospede(hospede, lista_hospedes)
    hospede.atribuir_quarto(quartos_por_numero[quartos_pedidos[posicao]])
    posicao = posicao + 1

print()
rececionista.listar_hospedes(lista_hospedes)

# reservas -david (teste)
reservas = []
for hospede in lista_hospedes:
    if hospede.quarto is not None:
        reservas.append(Reserva(hospede, hospede.quarto, hospede.dias_estadia))

print("\n Reservas ")
for reserva in reservas:
    reserva.mostrar_informacoes()

# tecnicos -edson(herança múltipla)
print("\n Técnicos ")
tecnico.registrar_reparo("Estores quebrado no quarto 102")
tecnico_rececao.registrar_hospede("Sofia")
tecnico_rececao.registrar_reparo("Torneira a pingar no quarto 202")
tecnico_rececao.mostrar_info()

# recepcionista -hery

print("\n Turno ")
rececionista.turno = "tarde"
rececionista.turno = "madrugada"   # inválido
print("Turno atual:", rececionista.turno)

# checkout -david
print("\n--- Contas e checkout ---")
total = 0
for hospede in lista_hospedes:
    conta = hospede.calcular_conta()
    print(f"Conta de {hospede.nome}: {conta:}€")
    total = total + conta
    hospede.checkout()
print(f"Total faturado: {total:}€")

# término de estadia -davidmain.
print("\n Quartos no fim ")
for quarto in quartos:
    quarto.mostrar_informacoes()