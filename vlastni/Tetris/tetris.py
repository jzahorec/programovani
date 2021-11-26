#!/usr/bin/python3
"""
Back-end tetrisu

Pri kazdem posunu dilku se vytvori novy, ktery se porovnava. Pokud novy dilek projde kontrolou,
puvodni se na nej prepise.
"""

import random

"""
Funkce na matici(seznam), potrebne pro otoceni dilku
"""


def transpozice(matice):  # transponuje matici
    transponovana_matice = [
        [None for j in range(len(matice))] for i in range(len(matice[0]))
    ]
    for i in range(len(matice)):
        for j in range(len(matice[0])):
            transponovana_matice[j][i] = matice[i][j]
    return transponovana_matice


def symetrie_radku(matice):  # prohodi prvky matice podle osy stredoveho sloupce
    symetricka_matice = [
        [matice[i][j] for j in range(len(matice[0]))] for i in range(len(matice))
    ]  # udela kopii
    delka_radku = len(matice[0])
    for radek in symetricka_matice:
        for i in range(delka_radku // 2):
            radek[i], radek[delka_radku - (i + 1)] = radek[delka_radku - (i + 1)], radek[i]

    return symetricka_matice


"""
Funkce na dilek
"""


def otoc(dilek, smer):  # vrati kontrolni dilek otoceny, smer True doleva
    pocet_radku = len(dilek.rozmery)
    pocet_sloupcu = len(dilek.rozmery[0])
    novy = Dilek()
    if smer:
        novy.rozmery = symetrie_radku(transpozice(dilek.rozmery))
    else:
        novy.rozmery = transpozice(symetrie_radku(dilek.rozmery))
    novy.i, novy.j = dilek.i + (pocet_radku - len(dilek.rozmery)), dilek.j + (
        pocet_sloupcu - len(dilek.rozmery[0])
    )  # vypocet zmeny pozice dilku
    return novy


def posun(dilek, smer):  # smer urcen ve tvaru [i, j], kde i, j jsou zmeny oproti puvodni
    novy = Dilek()
    novy.rozmery = [
        [dilek.rozmery[i][j] for j in range(len(dilek.rozmery[0]))]
        for i in range(len(dilek.rozmery))
    ]
    novy.i = dilek.i + smer[0]
    novy.j = dilek.j + smer[1]
    return novy


def kontrola(hraci_pole, dilek):
    # kontroluje, jestli dilek v poli
    if (
        dilek.i < 0
        or dilek.j < 0
        or dilek.i > len(hraci_pole) - len(dilek.rozmery)
        or dilek.j > len(hraci_pole[0]) - len(dilek.rozmery[0])
    ):
        return False

    lze = True

    for tmp_i in range(len(dilek.rozmery)):
        for tmp_j in range(len(dilek.rozmery[0])):
            if (
                hraci_pole[tmp_i + dilek.i][tmp_j + dilek.j]
                and dilek.rozmery[tmp_i][tmp_j]
            ):
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
            if not bod:
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
        if bod:
            return True
    return False


"""
Tridy pro hru
"""


class Dilek:  # instance dilku
    def __init__(self):
        self.rozmery = []
        self.i = 0
        self.j = 0

    def novy_dilek(self, hraci_pole):
        typy_dilku = [
            [[1], [1], [1], [1]],
            [[1, 0], [1, 0], [1, 1]],
            [[0, 1, 1], [1, 1, 0]],
            [[1, 1], [1, 1]],
            [[0, 1, 0], [1, 1, 1]],
        ]  # myslim, ze mam vsechny typy dilku
        barva = random.randint(1, 8)
        self.rozmery = typy_dilku[random.randint(0, len(typy_dilku) - 1)]
        for radek in range(len(self.rozmery)): # cislo znaci barvu, spravuje grafika
            for bod in range(len(self.rozmery[radek])):
                self.rozmery[radek][bod] *= barva
        if random.randint(0, 1):
            self.rozmery = transpozice(self.rozmery)

        self.i, self.j = 0, len(hraci_pole[0]) // 2 - len(self.rozmery[0]) // 2


class Hra:  # instance jedne hry
    def __init__(self, rozmery):
        self.hraci_pole = [[0 for j in range(rozmery[1])] for i in range(rozmery[0])]
        self.skore = 0
        self.dilek = Dilek()
        self.dilek.novy_dilek(self.hraci_pole)

    def otoc(self, smer):
        novy = otoc(self.dilek, smer)
        if kontrola(self.hraci_pole, novy):
            self.dilek = novy

    def posun(self, smer=[0, -1]):
        novy = posun(self.dilek, smer)
        if kontrola(self.hraci_pole, novy):
            self.dilek = novy

    def tick(self):  # klasicky pohyb dilku v case
        novy = posun(self.dilek, [1, 0])
        if kontrola(self.hraci_pole, novy):
            self.dilek = novy
        else:
            for i in range(len(self.dilek.rozmery)):  # zanoreni dilku do pole
                for j in range(len(self.dilek.rozmery[0])):
                    if self.dilek.rozmery[i][j]:
                        self.hraci_pole[i + self.dilek.i][j +
                                                          self.dilek.j] = self.dilek.rozmery[i][j]

            self.hraci_pole, body = vynulovani_radku(self.hraci_pole)
            self.skore += body

            if prohra(self.hraci_pole):
                return True
            else:
                self.dilek.novy_dilek(self.hraci_pole)

    def vykresli(self):  # vrati aktualbi pole i s vnorenym dilkem
        vykreslene_pole = [
            [self.hraci_pole[i][j] for j in range(len(self.hraci_pole[0]))]
            for i in range(len(self.hraci_pole))
        ]  # kopie hraciho pole

        for i in range(len(self.dilek.rozmery)):  # zanoreni dilku do pole
            for j in range(len(self.dilek.rozmery[0])):
                if self.dilek.rozmery[i][j]:
                    vykreslene_pole[i + self.dilek.i][j + self.dilek.j] = self.dilek.rozmery[i][j]

        return vykreslene_pole
