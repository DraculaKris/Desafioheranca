class Bebida:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo


class Refrigerante(Bebida):
    def __init__(self, nome, tipo, marca):
        super().__init__(nome, tipo)
        self.marca = marca


class Cafe(Bebida):
    def __init__(self, nome, tipo, temperatura):
        super().__init__(nome, tipo)
        self.temperatura = temperatura


Coca = Refrigerante('Coca-Cola zero', 'Com gás', 'Coca Cola')

Cafezin = Cafe('Café Vó Rosa', 'Extra Forte', 'Quente')

print(Coca.marca)
print(Cafezin.temperatura)