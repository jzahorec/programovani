"""
Prvni pokus o implementaci hry Tetris - zapoctovy program

Idea je dat kazdemu dilku pole, ktere si bude vyhodnocovat a pri svem zaniku se do pole zapise a privola dalsi dilek, kteremu doda aktualizovane pole
Pri zapisu se provede kontola radku, jestli neni nejaky plny, a pokud ano, pak tento radek se smaze a na zacatek se prida prazdny radek

Provest matiku na toceni dilkem, nejaka matice asi
"""

import random

"""
Funkce na matici
"""

def transpozice(matice): #transponuje matici
    transponovana_matice = [[None for j in range(len(matice))] for i in range(len(matice[0]))]
    for i in range(len(matice)):
        for j in range(len(matice[0])):
            transponovana_matice[j][i] = matice[i][j]
    return transponovana_matice

def symetrie_radku(matice): #prohodi prvky matice podle osy stredoveho sloupce
    delka_radku = len(matice[0])
    for radek in matice:
        for i in range(delka_radku // 2):
            radek[i], radek[delka_radku - (i + 1)] = radek[delka_radku - (i + 1)], radek[i]
    return matice

"""
Funkce na dilek
"""

def otoc(dilek, smer): #vrati kontrolni dilek otoceny podle zadani, smer True doleva
    pocet_radku = len(dilek.rozmery)
    pocet_sloupcu = len(dilek.rozmery[0])
    novy = Dilek
    if smer:
        novy.rozmery = symetrie_radku(transpozice(dilek.rozmery))
    else:
        novy.rozmery = transpozice(symetrie_radku(dilek.rozmery))
    novy.i, novy.j = dilek.i + (pocet_radku - len(dilek.rozmery)), dilek.j + (pocet_sloupcu - len(dilek.rozmery[0])) #vypocet zmeny pozice dilku
    return novy

def posun(dilek, smer):
    novy = Dilek
    novy.rozmery = dilek.rozmery
    novy.i = dilek.i + smer[0]
    novy.j = dilek.k + smer[1]
    return novy

def kontrola(hraci_pole, dilek):
    if dilek.i < 0 or dilek.j < 0 or dilek.i >= len(hraci_pole) - len(dilek.rozmery) or dilek.j >= len(hraci_pole[0]) - len(dilek.rozmery[0]): #kontroluje, jestli dilek v poli
        return False

    lze = True

    for tmp_i in range(len(dilek.rozmery)):
        for tmp_j in range(len(dilek.rozmery[tmp_i])):
            if self.hraci_pole[tmp_i + dilek.i][tmp_j + dilek.j] == 1:
                lze = False
    return lze

"""
Funkce na hraci pole
"""

def vynulovani_radku(hraci_pole):
    delka_radku = len(hraci_pole[0])
    plne_radky = []
    for i in range(len(hraci_pole)):
        plny = True
        for bod in hraci_pole[i]:
            if bod == 0:
                plny = False
                break
        if plny:
            plne_radky.append(i)

    for i in plne_radky:
        hraci_pole.pop(i)
        hraci_pole.insert(0, [0 for i in range(delka_radku)])
    body = len(plne_radky)
    return hraci_pole, body

def prohra(hraci_pole):
    for bod in hraci_pole[0]:
        if bod == 1:
            return True
    return False

"""
Tridy pro hru
"""

class Dilek: #instance dilku
    def __init__(self):
        self.rozmery = []
        self.i = 0
        self.j = 0

    def novy_dilek(self, hraci_pole):
        typy_dilku = [[[1],[1],[1],[1]], [[1, 0], [1, 0], [1, 1]], [[0, 1, 1], [1, 1, 0]], [[1, 1],[1, 1]], [[0, 1, 0], [1, 1, 1]]] #myslim, ze mam vsechny typy dilku
        self.rozmery = typy_dilku[random.randint(0, len(typy_dilku) - 1)]
        if random.randint(0, 1):
            self.rozmery = transpozice(self.rozmery)

        self.i, self.j = 0, len(hraci_pole[0]) // 2 - len(self.rozmery) // 2

class Game: #instance jedne hry
    def __init__(self, rozmery):
        self.hraci_pole = [[0 for j in range(rozmery[1])] for i in range(rozmery[0])]
        self.score = 0
        self.dilek = Dilek.novy_dilek()

    def otoc(self, smer):
        novy = otoc(self.dilek, smer):
        if kontrola(novy):
            self.dilek = novy

    def posun(self, smer=[0, -1]):
        novy = posun(self.dilek, smer)
        if kontrola(novy):
            self.dilek = novy

    def tick(self):
        novy = posun(self.dilek, [1, 0])
        if kontrola(novy):
            self.dilek = novy
        else:
            for i in range(len(self.dilek)): # zanoreni dilku do pole
                for j in range(len(self.dilek[0])):
                    self.hraci_pole[i+self.dilek.i][j+self.dilek.j] = self.dilek[i][j]

            self.hraci_pole, body = vynulovani_radku(self.hraci_pole)
            self.body += body

            if prohra(self.hraci_pole):
                return False, self.body
            else:
                return True
