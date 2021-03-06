#1. Carl Friedrich Gauss a fost un matematician german renumit pentru realizările sale științifice.
#Printre acestea, ne-a arătat faptul că suma primelor n numere naturale se poate calcula folosind formula:
#Cerință. Se citește de la tastatură un număr natural n. Să se afișeze suma primelor n numere.
n1 = 87
sum_n1 = n1*(n1+1)/2
print(int(sum_n1))

#2. Se citesc de la tastatură două cifre nenule și diferite. Afișați cele două numere care se pot realiza cu aceste cifre.
x2 = 3
y2 = 5
xy = x2 * 10 + y2
yx = y2 * 10 + x2
print(xy, yx)
 #3. Realizați un program care citește de la tastatură două numere naturale nenule și afișează suma, diferența, produsul, câtul și restul împărțirii lor.

#4. Un dog german a alergat n ture de teren de tenis care are dimensiunile standard: 23.77m x 8.23m. Ce distanță a parcurs el?
n4 = 8
lung = 23.77
lat = 8.23
perimetru = n4 * (lung + lat) * 2
print(perimetru, 'm')
"""Indicație. Atenție la perimetru. Se citește de la tastatură doar numărul de ture, notat cu n.

5. Se citește un număr natural format din exact trei cifre. Afișați numărul care conține toate cifrele micșorate cu 1.

Exemplu. Pentru numărul 359, se va afișa 248."""

n5 = 145
n5_3 = int(n5 % 10)
n5_2 = int(((n5 - n5_3) / 10) % 10)
n5_1 = int((n5 - n5_3 - n5_2 * 10)/100)
inv_mic = (n5_3 - 1) * 100 + (n5_2 - 1) * 10 + n5_1-1
print(inv_mic)
"""6. Se citește un număr natural format din exact două cifre. Afișați suma cuburilor cifrelor sale.

Exemplu. Pentru numărul 49, se va afișa 43+93, adică 793."""

n6 = 49
n6_3 = int(n6 % 10)
n6_2 = int(((n6 - n6_3) / 10) % 10)
print(n6_2**3 + n6_3**3)


"""7. Se citesc două numere naturale în variabilele x și y. Afișați valoarea expresiei: x2 + y2 - 23."""
x7 = 3
y7 = 267
print(x7**2 + y7**2 - 23)

"""Se citesc 4 numere întregi. Să se decidă dacă sunt distincte (adică nu există două egale între ele).

Indicație. Se compară primul număr cu toate celelalte, al doilea cu cele care îi urmează, al treilea cu al patrulea. 
Dacă în nici o comparaţie nu rezultă egalitate, se tipăreşte mesajul corespunzător..."""

a, b, c, d = input("a, b, c, d:").split()
if a != b and a!= c and a != d and b != c and b != d and c != d:
    print("all distinct")
else:
    if a == b:
        print("val a egal cu b")
    elif a == c:
        print("val a egal cu c")
    elif a == d:
        print("val a egal cu d")
    elif b == c:
        print("val b egal cu c")
    elif b == d:
        print("val b egal cu d")
    else:
        print("val c egal d")

#Se citesc trei valori reale a, b, c. Să se precizeze dacă ele pot fi laturile unui triunghi

a5, b5, c5 = input("a5, b5, c5:").split()
if a5 + b5 < c5:
    print("Cu numerele ", a5, b5, c5, "poti face un triunghi")
elif a5 + c5 < b5:
    print("Cu numerele ", a5, b5, c5, "poti face un triunghi")
elif b5 + c5 < a5:
    print("Cu numerele ", a5, b5, c5, "poti face un triunghi")
else:
    print("Cu numerele ", a5, b5, c5, "nu poti face un triunghi")

a5, b5, c5 = input("a5, b5, c5:").split()
if a5 + b5 > c5 and a5 + c5 > b5 and b5 + c5 > a5:
    print("Cu numerele ", a5, b5, c5, "poti face un triunghi")
else:
    print("Cu numerele ", a5, b5, c5, "nu poti face un triunghi")

# 5. Se citesc 3 numere intregi. Să se tipărească, dacă există, numărul care este egal cu suma celorlalte două.
#a6, b6, c6 = input("a6, b6, c6:").split()
a6 = int(input("a6:"))
b6 = int(input("b6:"))
c6 = int(input("c6:"))
if a6+b6 == c6:
    print(c6, "c ul")
elif a6 + c6 == b6:
    print(b6, "b ul")
elif c6 + b6 == a6:
    print(a6, "a ul")
else:
    print("no can do")

print(a6 + c6 == b6)
print(a6 + c6)
print(a6, b6, c6)
