import random

numero = random.randint(1, 10)
vidas = 3
pista = numero % 2 == 0
print("¡Bienvenido al juego de Adivina el Número!")
while vidas > 0:
    intento = input("Adivina un número entre 1 y 10: ")
    if not intento.isdigit() or not (1 <= int(intento) <= 10):
        print("Por favor, ingresa un número válido entre 1 y 10.")
        continue
    intento = int(intento)
    if intento == numero:
        print("¡Felicidades! Has adivinado el número correctamente.")
        break
    else:
        vidas -= 1
        if vidas == 0:
            print(f"Lo siento, has perdido. El número era {numero}.")
        else:
            print(f"Número incorrecto. Te quedan {vidas} vidas.")
            if pista:
                print("Pista: El número es par.")
            else:
                print("Pista: El número es impar.")
