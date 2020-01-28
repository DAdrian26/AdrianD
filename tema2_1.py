""""
Citeste de la tastatura un numar x
- afiseaza pe ecran suma cifrelor sale.
- daca toate cifrele sale sunt pare, afiseaza un mesaj care sa arate asta
- afiseaza numarul cifrelor pare si impare ale lui x
- afiseaza suma cifrelor pare si suma cifrelor impare
- afiseaza daca numarul este palindrom* sau nu (palindrom = citind cifrele sale de la dreapta la stânga se obţine acelaşi număr ex 12321)
)
nr = input("Alege un numar")
sum = 0
a = [int(i) for i in str(nr)]
for i in range(len(a)):
    sum += a[i]
print("Suma cifrelor este :", sum)

"""
nr_par =0
nr_impar =0
par = True
sum = 0
inv=0
sum_par=0
sum_impar=0
nr = int(input("Alege un numar"))
x=nr
while nr != 0 :
    cifra = nr % 10
    sum = sum + cifra
    inv = (inv * 10) + (nr % 10)
    nr = nr // 10

    if (cifra % 2 == 0):
        nr_par= nr_par +1
        sum_par= sum_par +cifra
    else:
        nr_impar = nr_impar +1
        sum_impar = sum_impar +cifra
        par = False

print("Suma numerelor este:" ,sum)

if par == True:
    print("Toate cifrele sunt pare")
else :
    print("Toate cifrele nu sunt pare")
#Verificare numar palindrom
if inv ==x :
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")

print("Numar cifre pare:" , nr_par)
print("Numar cifre impare:" , nr_impar)
print("Suma pare: ", sum_par)
print("Suma impare:",sum_impar)









