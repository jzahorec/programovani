# 100 patrovy dum, 1 vejce, z jakeho poschodi muzu shodit vejce abych ho chytil? 
# 100 pater, 10 vajec, jake patro? -1 vejce, 50, -2 vejce, 25, -3 vejce 13, -4 vejce 7, -5 vejce 4, -6 vejce 2, -7 vejce 1

#vajicka cca x(x-1)/2 = 100


def kvadr_rovnice(a, b, c):
    D = pow(b, 2) - 4*a*c
    if D < 0:
        return None
    elif D != 0: 
        x1 = (-b + pow(D, 0.5)) / (2 * a)
        x2 = (-b - pow(D, 0.5)) / (2 * a)
        return x1, x2
    else: 
        x = (-b + pow(D, 0.5)) / (2 * a)
        return x

# a, b, c = float(input()), float(input()), float(input())
# print(kvadr_rovnice(a, b, c))

def soucet_n(n):
    vysledek = 0
    for cislo in range(1, n+1):
        vysledek += cislo
    return vysledek

print(soucet_n(int(input())))