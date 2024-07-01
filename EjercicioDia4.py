from random import randint
print("##############################")
print("###  Adivino el Numero  ######")
print("##############################")
nombre = input("Decime tu nombre:")
print(f"Bueno {nombre}, he pensado un numero entre 1 y 100, y tienes solo OCHO intentos para adivinar cual crees que es el nuermo")
intentos = 8
resultado = randint(0,100)
valor = int(input("intenta adivinar: "))
while intentos > 0:
    if valor > 100 or valor < 0:
        intentos = intentos -1
        valor = int(input("el valor esta fuera de rando, eleji otro: "))
    elif valor < resultado:
        intentos = intentos -1
        valor = int(input("el num que ingresastes es muy chico intenta otro: "))
    elif valor > resultado:
        intentos = intentos -1
        valor = int(input('el numero que ingresaste es muy grande intenta otro: '))
    else:
        print(f"ACERTASTE con el numero {valor} en solo {8 - intentos}!!!")
        break

if intentos == 0:
    print("lo siento")
