from funcionarios import Funcionario, Recepcionista

class TecnicoManuntencao(Funcionario):
    def __init__(self, nome, idade, salario, especialidade):
        super():self.__init__(nome, idade, salario)
        self.especialidade = especialidade

    def reparar(self, quarto):
        print(f"{self.nome}está a reparar o {quarto}")

class TecnicoRecepcao(TecnicoManuntencao, Recepcionista):
    def __init__(self, nome, idade, salario, especialidade, setor):
        TecnicoManuntencao.__init__(self, nome, idade, salario, setor, especialidade)
        self.setor = setor