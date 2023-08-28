class Empregado:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


class Gerente(Empregado):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor


Mandante = Gerente('Kris', 6000, 'Controle de estoque')

print(Mandante.setor)