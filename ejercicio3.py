class Figura:
    def __init__(self):
        return
    def calcularArea(self):
        return
    def calcularPerimetro(self):
        return
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def calcularArea(self):
        return self.altura*self.base
    def calcularPerimetro(self):
        return self.altura*2+self.base*2
class Circulo(Figura):
    def __init__(self, radio):
        self.radio=radio
    def calcularArea(self):
        return self.radio*self.radio*3.14
    def calcularPerimetro(self):
        return 2*self.radio*3.14
class Triangulo(Figura):
    def __init__(self, cateto1, cateto2, hipotenusa):
        self.cateto1=cateto1
        self.cateto2=cateto2
        self.hipotenusa=hipotenusa
    def calcularArea(self):
        return (self.cateto1*self.cateto2)/2
    def calcularPerimetro(self):
        return self.cateto2+self.cateto1+self.hipotenusa
lista=[Rectangulo(4, 12), Circulo(5), Triangulo(3, 4, 5)]
for i in range(0, 3):
    print("Area:", lista[i].calcularArea())
    print("Perimetro:", lista[i].calcularPerimetro())