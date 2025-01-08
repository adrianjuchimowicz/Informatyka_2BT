# liczby8 = []
# with open("liczby1.txt") as plik:
#     for linia in plik:
#         liczby8.append(linia.strip())
# print(liczby8)
# minimum = int(liczby8[0])
# maks = int(liczby8[0])
# for i in range(1,len(liczby8)):
#     if minimum > int(liczby8[i]):
#         minimum = int(liczby8[i])
#     if maks < int(liczby8[i]):
#         maks = int(liczby8[i])
# print(maks,minimum)
# liczby8 = []
# with open("liczby2.txt") as plik:
#     for linia in plik:
#         liczby8.append(linia.strip())
#
# pierwszy = int(liczby8[0])
# ilosc = 1
# maksymalna_ilosc = 0
# for i in range(len(liczby8)-1):
#     if int(liczby8[i])<= int(liczby8[i+1]):
#         ilosc += 1
#         if ilosc > maksymalna_ilosc:
#             maksymalna_ilosc = ilosc
#     else:
#         ilosc = 1
# print(maksymalna_ilosc)


liczby8 = []
with open("liczby2.txt") as plik:
    for linia in plik:
        liczby8.append(linia.strip())

licznik = 0
for i in range(len(liczby8)):
    pass