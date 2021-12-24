# Se citeşte un număr natural n. Să se tipărească numărul obţinut prin inversarea poziţiilor cifrelor pe care le ocupă numărul citit.
# Exemplu. Dacă citim n=248, se va tipări 842.
# n = int(input("numarul de inversat este:"))
n = 248
inv = 0
# print(n/10)
# print(n//10)
# print(n%10)
while n !=0:
    inv = inv * 10 + n%10
    n = n//10
print(inv)


