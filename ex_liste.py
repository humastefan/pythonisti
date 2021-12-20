prenume = ['Mihai','George','Ana','Dan','Ion','Geta','Vio']
varsta = [14, 23, 15, 14, 12, 41, 39]
#a) Cosiderând că fiecare persoană are asociată vârsta pe același indice, afișați precum mai jos:
# Mihai are varsta de 14 ani.
# George are varsta de 23 de ani.

for i in range(len(prenume)):
    print(f"{prenume[i]} are varsta de {varsta[i]} ani.")

#b) Adăugați în liste la final, corespunzător, datele: Andreea, 34 și Ioan, 23. Tipăriți ambele liste apoi.
prenume.append("Andreea")
prenume.append("Ioan")
varsta.append(34)
varsta.append(23)
# prenume.remove("Ana")
print(prenume)
print(varsta)
dasas = prenume.index("Ana")
print(dasas, "aici este Ana")
print(prenume.pop("Ana"))
# c) Ștergeți datele din ambele liste despre Ana (atenție la indici).
if "Ana" in prenume:
    varsta.pop(prenume.pop(prenume.index("Ana")))
    prenume.remove("Ana")
print(prenume, varsta)
# d) Afișați primele trei elemente din lista prenume.
#
# e) Afișați lista prenume de la dreapta la stânga.
#
# f) Tipăriți elementele cu indicii 2 și 4, apoi de la 0 la 5 din ambele liste.