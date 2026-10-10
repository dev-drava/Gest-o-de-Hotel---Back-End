from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario, id_func=None, **kwargs):
        super().__init__(nome, idade, **kwargs)
        self._salario = None
        self.salario = salario
        self._id_func = id_func


    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("O salário não pode ser negativo")
        self._salario = valor

    @property
    def id_func(self):
        return self._id_func

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | "
              f"ID: {self.id_func} | Salario: {self.salario: .2f}")


class Gerente(Funcionario):
    BONUS_PERCENTAGEM = 0.10

    def __init__(self, nome, idade, salario, id_func=None, **kwargs):
        super().__init__(nome, idade, salario, id_func, **kwargs)

    def calcular_bonus(self):
        return self.salario * self.BONUS_PERCENTAGEM

    def mostrar_informacoes(self):
        super().mostrar_informacoes(self):
        print(f"Bónus: {self.calcular_bonus():.2f}€ | "
              f"Total: {self.salario + self.calcular_bonus():.2f}€")

    def gerar_relatorio(self, funcionarios):
        print("-Relatório de Funcionários-")
        for f in funcionarios:
            f.mostrar_informacoes() # polimorfismo
            print("-" * 30)

