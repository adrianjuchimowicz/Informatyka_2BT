ciagi = []
with open("ciagi.txt") as plik:
    for linia in plik:
        ciagi.append(linia.strip())
print(ciagi)

for i in range(len(ciagi)):
    if ciagi[i][:len(ciagi[i])//2] == ciagi[i][len(ciagi[i])//2:]:
        print(ciagi[i])

licznik = 0;
for i in range(len(ciagi)):
    if "11" not in ciagi[i]:
        licznik += 1
print(licznik)


def horner(liczba,x):#liczba - string, x - system w którym jest liczba w = int(liczba[0])
    for i in range(1,len(liczba)):
        w=0
        w = x * w + int(liczba[i])
        return w

liczba = []

for i in range(len(ciagi)):
    liczba.append(horner(ciagi[i],2))
print(liczba)

sito = []
for i in range (363000):
    sito.append(1)
for i in range(2,363000):
    if sito [i] ==1:
        for j in range(i+i,363000,i):
            sito[j]=0
pierwsza = []
for i in range(2,363000):
    if sito[i] == 1:
        pierwsza.append(i)
print(pierwsza)

for i in range(len(liczba)):
    czynniki = []
    for j in range(len(pierwsza)):
        liczba = liczba[i]
        while liczba % pierwsza[j] == 0:
            czynniki.append(pierwsza[j])
            liczba = liczba // pierwsza[j]
            if len(czynniki)>2:
                break
    if len(czynniki) == 2:
        print(liczba[i],czynniki)