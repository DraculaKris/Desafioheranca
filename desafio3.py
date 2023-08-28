class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

class Livro(Produto):
    def __init__(self,nome,preco,paginas):
        super().__init__(nome,preco)
        self.paginas = paginas

class Eletronico(Produto):
    def __init__(self,nome,preco,voltagem):
        super().__init__(nome,preco)
        self.voltagem = voltagem

Valor = Livro('As aventuras de Yan', 100,400)
print('PRODUTO 1:')
print(f'O nome do livro é {Valor.nome} seu preço é {Valor.preco} o números de páginas {Valor.paginas} páginas')

Valor1 = Eletronico('Iphine 15', 10000,100)
print('PRODUTO 2:')
print(f'O nome do eletrônico é {Valor.nome} seu preço é {Valor.preco} o números da voltagem do produto é {100} voltes')
