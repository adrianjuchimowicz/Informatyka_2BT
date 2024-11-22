def f(x):
    return x*x+1

a = 0
b = 2
E = 1000
calka = 0
szer = (b-a)/E
for i in range(E):
    wys = f(a + i * szer)
    calka += szer * wys

print(calka)