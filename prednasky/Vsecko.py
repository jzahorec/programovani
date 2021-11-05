"""
a = 5
b = 5.5
c = "nazdar"
teplota = 22
if(teplota >10):
	print("Hura do hostince!")
	print("A dam si Konrada 11.")
	print("A nakonec bude treba zaplatit.")
else:
	print("Nas nic nezadrzi! I tak jdeme - vime kam.")
"""

"""
prvni = int(input())
druhe = int(input())
if (druhe==0):
	print(prvni)

if druhe > prvni:
	prvni, druhe = druhe, prvni


while druhe > 0:
	#pom = prvni%druhe
	#prvni = druhe
	#druhe = pom
	prvni, druhe = druhe, prvni%druhe
print(prvni)
"""

"""
cislo = int(input())

if cislo == 0: print("0")

while (cislo>0):
	print(cislo%2, end="", sep="")
	cislo //= 2
"""

"""
cislo = int(input())
kandidat = 2
while(kandidat<cislo):
	if (cislo%kandidat == 0):
		print(kandidat, end="*")
		cislo //= kandidat
	else:
		kandidat += 1

print(cislo)
"""

"""
a = []
for i in range(10):
	a.append(i+1)

print(a[1:4])
"""

cislo = "2021"
hodnota = 0
for i in cislo:
	hodnota = hodnota*10 + ord(i)-48
print(hodnota)
