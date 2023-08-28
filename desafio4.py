class Marca:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Moto(Marca):
    def __init__(self,marca,modelo,ano,rodas):
        super().__init__(marca,modelo,ano)
        self.rodas = rodas

class Carro(Marca):
    def __init__(self,marca,modelo,ano,rodas):
        super().__init__(marca,modelo,ano)
        self.rodas = rodas

valor = Moto('Honda','Cb1000',2020,2)
print(f'Modelo {valor.modelo}, a marca {valor.marca} o ano é {valor.rodas}')

valor2 = Carro ('BMW','X6',2020,4)
print(f'Modelo {valor2.marca}, a marca {valor2.marca} o ano é {valor2.rodas}')
