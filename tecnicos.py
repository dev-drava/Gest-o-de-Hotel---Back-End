from funcionarios import Funcionario, Recepcionista

class TecnicoManutencao(Funcionario):
    def __init__(self, nome, idade, salario, especialidade):
        super().__init__(nome, idade, salario)
        self.especialidade = especialidade

    def reparar(self, quarto):
        print(f"{self.nome} está a reparar o {quarto}")

class TecnicoRecepcao(TecnicoManutencao, Recepcionista):
    def __init__(self, nome, idade, salario, especialidade, setor):
        TecnicoManutencao.__init__(self, nome, idade, salario, especialidade)
        self.setor = setor