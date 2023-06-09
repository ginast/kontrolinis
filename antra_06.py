"""Susikurti klasę “Figūra”, kuri saugoja ilgį ir plotį. Klasė turi turėti metodus plotui ir perimetrui apskaičiuoti ir grąžinti

Susikurti klasę “Stačiakampis”, kuris paveldi iš “Figūra”. Stačiakampio klasėje turi būti įgyvendinti stačiakampio ploto
ir perimetro skaičiavimo metodai.

Susikurti klasę “StatusisTrikampis”, kuris paveldi iš “Figūra”. Trikampio klasėje turi būti įgyvendinti stačiojo trikampio ploto
ir perimetro skaičiavimo metodai.

Susikurti bent po vieną stačiakampį ir trikampį, atspausdinti jų plotus ir perimetrus

# Testing the classes
rectangle = Rectangle(5, 10)
triangle = RightTriangle(3, 4)

print("Rectangle Information:")
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())
print()

print("Right Triangle Information:")
print("Area:", triangle.calculate_area())
print("Perimeter:", triangle.calculate_perimeter())
"""

import math
class Figura():
    def __init__(self, ilgis, plotis):
        self.ilgis = ilgis
        self.plotis = plotis

    def apskaiciuoti_plota(self):
        return self.ilgis *self.plotis

    def apskaiciuoti_perimetra(self):
        return (self.plotis+self.ilgis)*2



class Staciakampis(Figura):
    pass

class StatusisTrikampis(Figura): # reikia C - istrizaines, tam reikia sukurti C
    def apskaiciuoti_perimetra(self):
        return (self.ilgis + self.plotis)+ math.sqrt(self.ilgis**2 + self.plotis**2)

    def apskaiciuoti_plota(self):
        return (self.ilgis *self.plotis)/2



staciakampis = Staciakampis(5, 10)
print(f"Staciakampio ilgis - {staciakampis.ilgis}, staciakampio plotas - {staciakampis.plotis}")
print("Staciakampio plotas:", staciakampis.apskaiciuoti_plota())
print("Staciakampio perimetras:", staciakampis.apskaiciuoti_perimetra())

trikampis = StatusisTrikampis(3,4)
print(f"Trikampio ilgis - {trikampis.ilgis}, trikampio aukstis - {trikampis.plotis}")
print("Trikampio plotas:", trikampis.apskaiciuoti_plota())
print("Trikampio perimetras:", trikampis.apskaiciuoti_perimetra())