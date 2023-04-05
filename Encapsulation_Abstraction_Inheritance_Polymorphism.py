from abc import abstractmethod, ABC


class FormaGeometrica(ABC):
    Pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")


class Patrat(FormaGeometrica):

    def __init__(self, latura, culoare):
        self.__latura = latura
        self.culoare = culoare

    def descrie_patrat(self):
        print(f"Patratul are culoarea {self.culoare}")

    def schimba_culoare(self, culoare_noua):
        self.culoare = culoare_noua

    @property
    def latura(self):
        pass

    @latura.getter
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, latura):
        self.__latura = latura

    @latura.deleter
    def latura(self):
        self.__latura = None

    def aria(self):
        aria = self.__latura ** 2
        return aria


class Cerc(FormaGeometrica):
    __raza = None

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        pass

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @raza.deleter
    def raza(self):
        self.__raza = None

    def aria(self):
        aria = self.__raza ** 2 * self.Pi
        return aria

    def descrie(self):
        print("Eu nu am colturi")


obiect_patrat = Patrat(4, "rosu")
obiect_cerc = Cerc(3)

print(f"Aria patratului este: {obiect_patrat.aria()} cm")
print(f"Latura patratului este: {obiect_patrat.latura} cm")
obiect_patrat.latura = 5
print(f"Latura patratului dupa update este: {obiect_patrat.latura} cm")
print(f"Aria patratului dupa update este: {obiect_patrat.aria()} cm")
del obiect_patrat.latura
print(f"Latura patratului dupa delete este: {obiect_patrat.latura} ")

print(f"Aria cercului este: {obiect_cerc.aria()} cm")
print(f"Raza cercului este: {obiect_cerc.raza} cm")
obiect_cerc.raza = 5
print(f"Raza cercului dupa update este: {obiect_cerc.raza} cm")
print(f"Aria cercului dupa update este: {obiect_cerc.aria()} cm")
del obiect_cerc.raza
print(f"Raza cercului dupa delete este: {obiect_cerc.raza} cm")
obiect_patrat.descrie_patrat()
obiect_patrat.schimba_culoare("roz")
obiect_patrat.descrie_patrat()
