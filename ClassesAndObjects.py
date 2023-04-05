import math
from tabulate import tabulate
from datetime import date

# 1
class Cerc():

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Culoarea cercului este {self.culoare} iar raza cercului este: {self.raza} cm")

    def aria_cerc(self):
        self.aria = self.raza ** 2 * math.pi
        return self.aria

    def diametru_cerc(self):
        self.diametru_cerc = 2 * self.raza

    def circumferinta_cerc(self):
        self.circumferinta_cerc = 3.14 * 2 * self.raza


Cerc1 = Cerc(12, "rosu")
Cerc2 = Cerc(7, "roz")
Cerc1.descrie_cerc()
Cerc2.descrie_cerc()
print(f"Cercul1 are culoarea {Cerc1.culoare}")
print(f"Cercul1 are raza: {Cerc1.raza} cm")
print(f"Cercul1 are aria: {Cerc1.aria_cerc()}")
print(f"Cercul2 are culoarea {Cerc2.culoare}")
print(f"Cercul2 are raza: {Cerc2.raza} cm")
print(f"Cercul2 are aria: {Cerc2.aria_cerc()}")


# 2
class Dreptunghi():

    def __init__(self, lungime, latime, culoare,):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghi(self):
        print(f"Dreptunghiul are o lungime de {self.lungime} cm, latime de {self.latime} cm si culoarea {self.culoare}")

    def aria_dreptunghi(self):
        self.aria = self.lungime * self.latime

    def perimetrul_dreptunghi(self):
        self.perimetrul = 2 * (self.lungime + self.latime)

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare


Dreptunghi1 = Dreptunghi(9, 5, "alb")
Dreptunghi1.descrie_dreptunghi()
Dreptunghi1.schimba_culoare('albastru')
Dreptunghi1.descrie_dreptunghi()


# 3
class Angajat():

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie_angajat(self):
        print(f"Numele de familie al angajatului este {self.nume}. ", "\n"
              f"Prenumele angajatului este {self.prenume}. ", "\n"
              f"Angajatul are un salar de {self.salariu} lei"),

    def nume_complet(self):
        self.nume_complet = self.nume + " " + self.prenume

    def salariu_lunar(self):
        self.salariu_lunar = self.salariu

    def salariu_anual(self):
        self.salariu_anual = self.salariu * 12

    def marire_salariu(self):
        self.salariu = (5 * self.salariu)/100 + self.salariu
        print(f"Salariul actualizat este {self.salariu} lei")


Angajat1 = Angajat("Tapu", "Andreea", 5000)
Angajat1.descrie_angajat()
Angajat1.marire_salariu()


# 4
class Cont():
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")

    def creditare_cont(self, suma):
        self.sold += suma

    def debitare_cont(self, suma):
        self.sold -= suma


Cont1 = Cont("RO72xxxxaaaajjjjxxxx0000", "Tapu Andreea", 2000)
Cont1.afisare_sold()
Cont1.debitare_cont(3000)
Cont1.creditare_cont(1500)
Cont1.afisare_sold()

# 5
class Factura():
    seria = "PYT"
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate_schimbata):
        self.cantitate = cantitate_schimbata

    def schimba_pretul(self, pret_schimbat):
        self.pret_buc = pret_schimbat

    def schimba_nume_produs(self, nume_produs_schimbat):
        self.nume_produs = nume_produs_schimbat

    def genereaza_factura(self):
        print(f"Factura seria {self.seria} numar {self.numar}")
        today = date.today()
        print("Data facturii este: ", today)
        date_factura = [["Produs", "Cantitate", "Pret_bucata", "Total"], [self.nume_produs, self.cantitate, self.pret_buc, self.cantitate*self.pret_buc]]
        print(tabulate(date_factura, headers='firstrow'))


Produs1 = Factura(111, "Ciocolata_Milka", 10, 6)
Produs2 = Factura(111, "Ciocolata_Kandia", 15, 8)
Produs1.schimba_cantitatea(13)
Produs1.schimba_pretul(7)
Produs1.schimba_nume_produs("Ciocolata_Milka_cu_lapte")
Produs1.genereaza_factura()

print("-----------------------")


# 6
class Masina():
    marca = "Audi"
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = "Gri"
    culori_disponibile = {"alba", "rosie", "neagra", "galbena", "verde", "albastra"}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie_masina(self):
        print(f"Masina este marca: {self.marca}", "\n"
              f"Modelul masinii este: {self.model}", "\n"
              f"Viteza maxima a masinii este: {self.viteza_maxima}", "\n"
              f"Viteza actuala a masinii este: {self.viteza_actuala}", "\n"
              f"Masina are culoarea: {self.culoare}", "\n"
              f"Masina este inmatriculata: {self.inmatriculata}")

    def inmatriculare_masina(self):
        self.inmatriculata = True
        return self.inmatriculata

    def vopseste_masina(self, culoare):
        self.culoare = culoare
        if culoare in self.culori_disponibile:
            print(f"Masina se va vopsi in culoarea {culoare}")
        else:
            print("Culoarea nu este disponibila")

    def accelereaza_masina(self, viteza_dorita):
        if viteza_dorita < 0:
            print("Eroare")
        elif viteza_dorita >= self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza_dorita
        print(f"Viteza actuala este: {self.viteza_actuala}")

    def franeaza_masina(self):
        self.viteza_actuala = 0
        print(f"Viteza actuala este: {self.viteza_actuala}. Am oprit masina")


Masina1 = Masina("A4", 220)
Masina1.descrie_masina()
Masina1.inmatriculare_masina()
print(Masina1.inmatriculata)
Masina1.vopseste_masina("albastra")
Masina1.accelereaza_masina(230)
Masina1.franeaza_masina()
