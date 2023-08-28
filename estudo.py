class Carro:
    def __init__(self,nome,cor,marca):
        self.nome = nome
        self.cor = cor
        self.marca = marca
    def Ligar (self):
        print('Ligando o',self.nome)

class Carro2:
    def __init__(self,ano):
        self.ano = ano
    def Farol(self):
        print('Acendendo as luzes')
    def Acelerador(self):
        print('Acelerando...')

class CarroCitroen(Carro,Carro2):
    def __init__(self,nome,cor,portas,ano):
        Carro.__init__(self,nome,cor,'Citroen') #isso ocorre quando se tem que acessar duas classes e não só uma,
        Carro2.__init__(self, ano)  #no caso não se utilizando super
        self.portas = portas

Car = CarroCitroen('Cactus','Azul',2,2022)




car1 = CarroCitroen('C3','Branco',4)
car2 = CarroCitroen('Cactus','Azul',2)