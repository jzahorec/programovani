"""
seznam bodu, kazdy bod N floating point dimenzi, oddelenych mezerami. n >= 2
vypis dva body nejbliz a jejich vzdalenost

pr
0.0 0.0
4.0 3.0
20.0 20.0

vystup
Points (0.0, 0.0) and (4.0, 3.0) are closest, with distance 5.0
"""
import math
import sys

vstup = sys.stdin.readlines()

body = [bod.strip().split() for bod in vstup]
for i in range(len(body)):
    for j in range(len(body[0])):
        body[i][j] = float(body[i][j])

vzdalenost = -1
vyherni = []
dimenze = len(body[0])

for i in range(len(body)):
    for j in range(i+1, len(body)):
        tmp_vzdalenost = 0
        for k in range(dimenze):
            tmp_vzdalenost += pow(body[i][k] - body[j][k], 2)
        tmp_vzdalenost = math.sqrt(tmp_vzdalenost)
        if vzdalenost == -1:
            vzdalenost = tmp_vzdalenost
            vyherni = [body[i], body[j]]
        if tmp_vzdalenost < vzdalenost:
            vzdalenost = tmp_vzdalenost
            vyherni = [body[i], body[j]]

print("Points", vyherni[0], "and", vyherni[1], "are closest, with distance", vzdalenost)
