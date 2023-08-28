class Forma:
    def __init__(self,largura,Altura):
        self.largura = largura
        self.Altura = Altura

class Retangulo(Forma):
    def __init__(self,largura1,Altura1):
        super().__init__(largura1,Altura1)

    def calc(self):
        area = (self.Altura * self.largura)
        return area


class Triangulo(Forma):
    def __init__(self, largura2, Altura2):
        super().__init__( largura2, Altura2)

    def calc(self):
        area = (self.Altura * self.largura)
        return area


Medidas = Retangulo(2,4)
print(Medidas.calc())

medidas2 = Triangulo(3,6)
print(medidas2.calc())


    
