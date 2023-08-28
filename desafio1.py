class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade,matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

valor = Aluno('Kris',16,'Sesi-136')
print(f'O aluno {valor.nome} tem {valor.idade} anos e estuda no {valor.matricula}')