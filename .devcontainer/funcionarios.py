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
