"""
Prvni pokus o implementaci hry Tetris - zapoctovy program

Idea je dat kazdemu dilku pole, ktere si bude vyhodnocovat a pri svem zaniku se do pole zapise a privola dalsi dilek, kteremu doda aktualizovane pole
Pri zapisu se provede kontola radku, jestli neni nejaky plny, a pokud ano, pak tento radek se smaze a na zacatek se prida prazdny radek
"""

hraci_pole = [[0] * 15] * 20

class Dilek:
    def __init__(self, hraci_pole, rozmery=[[1, 1], [1, 1]]):
        self.rozmery = rozmery
        self.hraci_pole = hraci_pole
        self.x, self.y = len(self.hraci_pole[0])//2 - len(self.rozmery[0])//2, 0

    def kontrola(self, smer=[1, 0]):
        lze = True
        for tmp_x in range(len(self.rozmery)):
            for tmp_y in range(len(self.rozmery[tmp_x])):
                if self.hraci_pole[tmp_x + self.x + smer[0]][tmp_y + self.y + smer[1]] == 1:
                    lze = False
        return lze

    def levo(self):
        if self.y > 0:
            self.y -= 1
    def pravo(self):
        if self.y < len(self.hraci_pole[0]) - len(self.rozmery[0]) - 1:
            self.y += 1
    def tick(self):

        pass

for radek in hraci_pole:
    for bod in radek:
        print(bod, end=" ")
    print()


dilek = Dilek(hraci_pole)

dilek = Dilek(dilek.hraci_pole, typy_dilku[random.randint(4)])

dilek.levo()

dilek.levo()

dilek.levo()

dilek.levo()

dilek.levo()
print(dilek.x, dilek.y)
