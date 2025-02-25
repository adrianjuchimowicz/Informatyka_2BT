def jednolity(napis):
    for i in range(len(napis)-1):
        if napis[i] != napis[i+1]:
            return False
    return True

lista_napisow = []
with open("dane_napisy.txt") as plik:
    for linia in plik:
        lista_napisow.append(linia.split())
print(lista_napisow)

licznik =0
licznik2 = 0
for napisyy in lista_napisow:
    if napisyy[0] == napisyy[1]:
        if jednolity(napisyy[0]):
            licznik2 +=1
print(licznik2)


for napisy in lista_napisow:
    if sorted(napisy[0]) == sorted(napisy[1]):
        licznik +=1
print(licznik)