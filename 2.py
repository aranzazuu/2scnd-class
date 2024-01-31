import random

contraseñas = []

def contraseña_nueva():
    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contraseña = ''.join(random.choice(caracteres) for _ in range(random.randint(8, 16)))
    return contraseña

while True:
    opcion = input("Para generar una contraseña nueva, coloca 1. Para revisar contraseñas generadas, coloca 2: ")

    if opcion == '1':
        contraseña = contraseña_nueva()
        print(contraseña)
        contraseñas.append(contraseña)

    elif opcion == '2':
        print(contraseñas)

    else:
        print("Elige una opción válida")
