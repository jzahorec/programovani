mnozina = [1, 2, 3, 4]


i = 0
N = 4
subset = []

size = int(input("size: "))
allowed = [int(input("val: ")) for _ in range(size)]

def suma(set):
    vysledek = 0
    for number in set:
        vysledek += number
    return vysledek

def subsets(i):
    if i == len(allowed):
        print(subset, suma(subset))
    else:
        subset.append(allowed[i])
        subsets(i+1)

        subset.pop()
        subsets(i + 1)


subsets(i)
