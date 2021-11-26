# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 09:10:27 2021

@author: jzahorec
"""

slovnik = []
dotazy = []

N = int(input())
for i in range(N):
    slovo = input()
    slovnik.append(slovo)
M = int(input())
for i in range(M):
    dotaz = input()
    dotazy.append(dotaz)

for dotaz in dotazy:
    presmycky = []
    pismena = {}
    for pismeno in dotaz:
        if pismeno in pismena:
            pismena[pismeno] += 1
        else:
            pismena[pismeno] = 1
    for slovo in slovnik:
        pismena_slova = {}
        for pismeno in slovo:
            if pismeno in pismena_slova:
                pismena_slova[pismeno] += 1
            else:
                pismena_slova[pismeno] = 1
        if pismena == pismena_slova:
            presmycky.append(slovo)
    for slovo in presmycky:
        print(slovo, end=" ")
    print()
