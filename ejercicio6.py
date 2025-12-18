import geometria

lista = [
    geometria.Rectangulo(4, 12),
    geometria.Circulo(5),
    geometria.Triangulo(3, 4, 5)
]
for i in range(0, 3):
    print("Area:", lista[i].calcularArea())
    print("Perimetro:", lista[i].calcularPerimetro())