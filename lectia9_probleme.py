"""1. Realizați un program care citește de la tastatură un șir de caractere și afișează de câte ori apare litera "a" în text.

Exemplu. Pentru "Mihai este la mare." se va afișa 3.

Rezolvare. Simplu – folosind metoda count():

s = input()
print(s.count("a"))

Exercițiu propus. Realizați un program similar care afișează de câte ori apare fiecare vocală din alfabetul
englezesc în textul citit și apoi la final, totalul aparițiilor lor. Atenție la detalii – mai jos e stilizat puțin rezultatul:"""

text = "Mihai este la mare capcaun."
# s = input()
# print(text.count("a"))
dictionar = {}
vocale = "aeiou"
for i in vocale:
    print("vocala", i, "este de", text.count(i), "ori in textul dat")
    dictionar[f"litera_{i}"] = text.count(i)
print(dictionar)

total = sum(dictionar.values())
print(total)

lista_mea = []
for i in vocale:
    lista_mea.append(text.count(i))
print(sum(lista_mea))
print(lista_mea, "haida")
print(lista_mea.sort(), "sortata")
print(type(lista_mea.sort()))
lista2 = lista_mea.sort()
print(type(lista2))
"""2. Realizați un program care citește de la tastatură un șir de caractere și afișează următoarele informații:

a) lungimea șirului
b) dacă există vreo apariție a consoanei "x"
c) dacă șirul începe cu "a" sau "A"
d) daca șirul se termină cu '.' """

# a) lungimea șirului
text2 = "Realizați un program care citește de la tastatură un șir de caractere și afișează următoarele informații:"
print("in textul dat sunt", len(text2), "de caractere.")

# b) dacă există vreo apariție a consoanei "x"
if "x" in text2:
    print("exista x")
else:
    print("x nu exista")

# c) dacă șirul începe cu "a" sau "A"
if text2.startswith("a"):
    print("incepe cu a")
elif text2.startswith("A"):
    print("incepe cu A")
else:
    print("textul dat incepe cu", f"'{text2[0]}'.")

# d) daca șirul se termină cu '.'

if text2.endswith("."):
    print("se termina cu '.'.")
else:
    print("textul dat se termina cu", f"'{text2[len(text2)-1]}'.")

"""3. Verificați dacă un șir de caractere citit are sau nu lungimea mai mare decât 20.
Exemplu. Pentru "Eric este un baiat istet in clasa a VII-a." se va afișa True."""
text3 = "3. Verificați dacă un șir de caractere citit are sau nu lungimea mai mare decât 20.\
Exemplu. Pentru 'Eric este un baiat istet in clasa a VII-a.' se va afișa True."
print(len(text3) > 20)

"""4. Fiind citite un nume de oraș, o țară și o cifră, afișați un text la alegere.
Exemplu. Pentru "Paris", "Franta" și "7" am tipărit "Super! Si eu am vizitat Franta, iar in Paris am petrecut minunat 7 zile"."""
tara = "input('tara:')"
oras = "input('oras:')"
numar_zile = "int(input('numar de zile:'))"
text_var = "Super! Si eu am vizitat %s, iar in %s am petrecut minunat %s zile."%(tara.capitalize(), oras.capitalize(), numar_zile)
print(text_var)

"""5. Se introduce un șir de caractere. Afișați-l cu majuscule, citit de la dreapta la stânga."""
text5 = "Se introduce un șir de caractere. Afișați-l cu majuscule, citit de la dreapta la stânga."
text5_rev = text5.upper()[::-1]
print(text5)
print(text5_rev)

"""6. Fiind citit un șir de caractere, afișați dacă primul caracter este identic cu ultimul introdus (True/False)."""
text6 = "6. Fiind citit un șir de caractere, afișați dacă primul caracter este identic cu ultimul introdus (True/False)."
#print(text6.endswith(text6[len(text6)-1]) == text6.startswith(text6[0]))
print(text6[0] == text6[len(text6)-1])

lista = [0, 1]



