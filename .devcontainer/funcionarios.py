from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario, id_func=None):
        super().__init__(nome, idade)
        self.salario = salario     
        self.id_func = id_func

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("O salário não pode ser negativo")
        self._salario = valor


    def mostrar_informacoes(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | "
              f"ID: {self.id_func} | Salário: {self.salario:.2f}")


class Gerente(Funcionario):
    BONUS_PERCENTAGEM = 0.10

    def calcular_bonus(self):
        return self.salario * self.BONUS_PERCENTAGEM

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Bónus: {self.calcular_bonus():.2f}€ | "
              f"Total: {self.salario + self.calcular_bonus():.2f}€")

    def gerar_relatorio(self, funcionarios):
        print("- Relatório de Funcionários -")
        for f in funcionarios:
            f.mostrar_informacoes()  # polimorfismo
            print("-" * 30)


class Recepcionista(Funcionario):
    TURNOS_VALIDOS = ("manhã", "tarde", "noite")

    def __init__(self, nome, idade, salario, turno, id_func=None, **kwargs):
        super().__init__(nome=nome, idade=idade, salario=salario,
                         id_func=id_func, **kwargs)
        self.turno = turno      

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, valor):
        valor = valor.lower()
        if valor not in self.TURNOS_VALIDOS:
            raise ValueError(f"Turno inválido. Use: {', '.join(self.TURNOS_VALIDOS)}")
        self._turno = valor

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Turno: {self.turno}")

    def registrar_hospede(self, hospede, lista_hospedes):
        lista_hospedes.append(hospede)
        print(f"Hóspede {hospede.nome} registrado.")

    def listar_hospedes(self, lista_hospedes):
        if not lista_hospedes:
            print("Não há hóspedes registrados")
            return
        for i, h in enumerate(lista_hospedes, start=1):
            print(f"{i}.", end=" ")
            h.mostrar_informacoes()