prenume = ['Mihai','George','Ana','Dan','Ion','Geta','Vio']
varsta = [14, 23, 15, 14, 12, 41, 39]
#a) Cosiderând că fiecare persoană are asociată vârsta pe același indice, afișați precum mai jos:
# Mihai are varsta de 14 ani.
# George are varsta de 23 de ani.

#for i in range(len(prenume)): # todo scoate ###
#    print(f"{prenume[i]} are varsta de {varsta[i]} ani.")

#b) Adăugați în liste la final, corespunzător, datele: Andreea, 34 și Ioan, 23. Tipăriți ambele liste apoi.
prenume.append("Andreea")
prenume.append("Ioan")
varsta.append(34)
varsta.append(23)

dasas = prenume.index("Ana")
print("Ana este la indexul", dasas, "din", prenume)
print(prenume)
print(varsta)

# c) Ștergeți datele din ambele liste despre Ana (atenție la indici).
varsta.pop(dasas)
prenume.pop(prenume.index("Ana"))
print(prenume)
print(varsta)

# d) Afișați primele trei elemente din lista prenume.
print(prenume[:3])
# e) Afișați lista prenume de la dreapta la stânga.
print(prenume[::-1])
# f) Tipăriți elementele cu indicii 2 și 4, apoi de la 0 la 5 din ambele liste.
print(prenume[2:5:2]) # primul 2 este primul indice printat, al doilea 2 este pasul intervalului printat
print(varsta[2:5:2])
print(prenume[:6]) # de la 0 la 5 inclusiv - deci fara 6
print(varsta[:6])
# Afisati inversul
print(varsta)
varsta.reverse() #similar cu linia 30

lista55 = [8,7,9,10,6,5,4]

# Ce va afișa comanda
print(max(lista55)//2)
print(sum(lista55)+max(lista55)//2)