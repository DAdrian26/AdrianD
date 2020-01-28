# PARTEA A DOUA
"""
Citeste de la tastatura numere pana se citeste valoarea 0. apoi:
- Sa se afiseze cel mai mare numar citit de la tastatura
- Sa se afiseze suma numerelor impare citite
- Sa se afiseze numarul maxim de numere citite consecutiv crescator
(exemplu:
1 2 3 0 -> 3 numere (1 2 3)
1 2 0 3 4 5 -> 3 numere (3 4 5)
5 3 2 0 -> 0 numere
5 3 1 2 -> 2 numere (1 2)
"""

sum_impar = 0
count_nr = 0
print("Se vor citi numere pana la intalnirea valori 0")
nr = int(input("Alege un numar"))
max=nr
if (nr % 2) == 1:
    sum_impar = sum_impar + nr

while nr != 0 :
    nr = int(input("Alege un numar"))
    if max < nr :
        max = nr
        # count_nr +=1
    if (nr % 2) == 1:
        sum_impar = sum_impar +nr
print("Maximul dintre numere este: ", max)
print("Suma numerelor impare este :", sum_impar)
print("Numarul maxim de numere citite consecutiv crescator este :",count_nr)