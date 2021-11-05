"""
Cows and bulls
nahodne 4ciferne cislo, pak user 4ciferne cislo, kazde uhodle cislo na spravnem miste je cow, kazde cislo spravne na spatnem miste je byk. jakmile je cislo spravne, hra konci
"""

import random


cislo = []
for i in range(4):
    cislice = random.randint(0, 9)
    cislo.append(str(cislice))

konec = False
while not konec:
    hadane_cislo = input("Enter a number:\n")
    cows = 0
    bulls = 0
    for i in range(len(hadane_cislo)):
        if hadane_cislo[i] == cislo[i]:
            cows += 1
        elif hadane_cislo[i] in cislo:
            bulls += 1
    print(f"Cows: {cows} \nBulls: {bulls}")
    if cows == 4:
        konec = True
        print("You won")
