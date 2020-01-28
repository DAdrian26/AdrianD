import random
generated =random.randint(0,100)
while True :
    x=int(input("Alege un numar"))
    if generated == x:
        print("Corect")
        break
    elif generated >x :
        print ("Caut un numar mai mare")
    else :
        print("Caut un numar mai mic")

