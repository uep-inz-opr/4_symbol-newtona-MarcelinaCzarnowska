import math

zmienne = map(int, input().split())
x = list(zmienne)

n = x[0]
k = x[1]
nk = n-k

wynik_n = []
wynik_k = []
wynik_nk = []

while n >= 1:
    wynik_n.append(n)
    n = n-1

while k >= 1:
    wynik_k.append(k)
    k = k-1
    