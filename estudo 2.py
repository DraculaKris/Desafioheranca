class Pessoa:
    def __init__(self,nome , idade):
        self.nome = nome
        self. idade = idade

    def Respirar(self):
        print('Respirando....')

class Aluno (Pessoa):
    def __init__(self,nome,idade,media,nota1):
        super().__init__(nome,idade)
        self.media = media
        self.nota1 = nota1

aluno1 = Aluno('Morelli',12,7,10)

class AlunoSESI(Aluno)