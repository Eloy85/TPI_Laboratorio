import os
import random

def valorNum(num, dificultad):
    if dificultad == 1:
        num = random.randint(1, 9)
    elif dificultad == 2:
        num = random.randint(1, 99)
    elif dificultad == 3:
        num = random.randint(1, 999)
    return num

def puntos(dificultad, punto):
    if dificultad == 1:
        punto += 10
        print("¡Correcto! Sumás 10 puntos.")
    elif dificultad == 2:
        punto += 20
        print("¡Correcto! Sumás 20 puntos.")
    elif dificultad == 3:
        punto += 30
        print("¡Correcto! Sumás 30 puntos.")
    return punto

salir = str()
a = 0
b = 0
puntaje = 0

tablaPosiciones = []

for j in range(11):
    tablaPosiciones.append([0] * 2)

tablaPosiciones[0] = "Roxana", 3000
tablaPosiciones[1] = "Francisco", 1500
tablaPosiciones[2] = "Roberto", 1000
tablaPosiciones[3] = "Elena", 500
tablaPosiciones[4] = "Sandra", 300
tablaPosiciones[5] = "Jorge", 250
tablaPosiciones[6] = "Ignacio", 100
tablaPosiciones[7] = "Zulema", 50
tablaPosiciones[8] = "Gaston", 20
tablaPosiciones[9] = "Pedro", 10


while salir != "n":
    print("****************************************************\n"
          "¡Bienvenido a MateMata! Elige una categoría")
    print("1 - SUMA \n2 - RESTA \n3 - MULTIPLICACION \n4 - DIVISION")
    tipoOperacion = 0
    while tipoOperacion == 0:
        try:
            tipoOperacion = int(input("Ingresa la opción elegida (1 - 4): "))
        except ValueError:
            print("Por favor ingresa un número.")
        else:
            while tipoOperacion > 4 or tipoOperacion < 1:
                tipoOperacion = int(input("Opción incorrecta. Ingresa la opción elegida (1 - 4): "))
    print("****************************************************\n"
          "Seleccione el nivel de dificultad (1 - 3)")
    print("1 - Fácil \n2 - Medio \n3 - Difícil")
    nivel = 0
    while nivel == 0:
        try:
            nivel = int(input())
        except ValueError:
            print("Por favor ingresa un número.")
        else:
            while nivel > 3 or nivel < 1:
                nivel = int(input("Opción incorrecta. Seleccione el nivel de dificultad (1 - 3): "))

    if tipoOperacion == 1:  # suma
        i = 0
        for i in range(10):
            a = valorNum(a, nivel)
            b = valorNum(b, nivel)
            print("*** Pregunta", i+1, "de 10 ***")
            print(a, "+", b, "=")
            resultado = int()
            while resultado != a+b:
                try:
                    resultado = int(input())
                except ValueError:
                    print("Por favor ingresa un número.")
                else:
                    if resultado == a + b:
                        puntaje = puntos(nivel, puntaje)
                    else:
                        print("Incorrecto. La respuesta correcta es", a + b)
                        break
        print("Fin de la ronda. Tu puntaje total es", puntaje)
    elif tipoOperacion == 2:  # resta
        i = 0
        for i in range(10):
            a = valorNum(a, nivel)
            b = valorNum(b, nivel)
            while a < b:
                a = valorNum(a, nivel)
                b = valorNum(b, nivel)
            print("*** Pregunta", i+1, "de 10 ***")
            print(a, "-", b, "=")
            resultado = int()
            while resultado != a - b:
                try:
                    resultado = int(input())
                except ValueError:
                    print("Por favor ingresa un número.")
                else:
                    if resultado == a - b:
                        puntaje = puntos(nivel, puntaje)
                    else:
                        print("Incorrecto. La respuesta correcta es", a - b)
                        break
        print("Fin de la ronda. Tu puntaje total es", puntaje)
    elif tipoOperacion == 3:  # multiplicación
        i = 0
        for i in range(10):
            a = valorNum(a, nivel)
            b = valorNum(b, nivel)
            print("*** Pregunta", i+1, "de 10 ***")
            print(a, "x", b, "=")
            resultado = int()
            while resultado != a * b:
                try:
                    resultado = int(input())
                except ValueError:
                    print("Por favor ingresa un número.")
                else:
                    if resultado == a * b:
                        puntaje = puntos(nivel, puntaje)
                    else:
                        print("Incorrecto. La respuesta correcta es", a * b)
                        break
        print("Fin de la ronda. Tu puntaje total es", puntaje)
    elif tipoOperacion == 4:  # división
        i = 0
        for i in range(10):
            a = valorNum(a, nivel)
            b = valorNum(b, nivel)
            while a % b != 0:
                a = valorNum(a, nivel)
                b = valorNum(b, nivel)
            print("*** Pregunta", i+1, "de 10 ***")
            print(a, "/", b, "=")
            resultado = int()
            while resultado != a / b:
                try:
                    resultado = int(input())
                except ValueError:
                    print("Por favor ingresa un número.")
                else:
                    if resultado == a / b:
                        puntaje = puntos(nivel, puntaje)
                    else:
                        print("Incorrecto. La respuesta correcta es", a // b)
                        break
        print("Fin de la ronda. Tu puntaje total es", puntaje)

    salir = str(input("¿Desea volver a jugar? S/N): "))
    while salir != "s" and salir != "n":
        salir = str(input("¿Desea volver a jugar? S/N): "))
    print("\n")

nombre = input("Ingresa tu nombre: ")

puesto = 0
for i in range(10):
    if puntaje < tablaPosiciones[i][1]:
        puesto = i + 1

if puntaje > tablaPosiciones[puesto][1]:
    for i in range(10, puesto, -1):
        tablaPosiciones[i] = tablaPosiciones[i - 1]

tablaPosiciones[puesto] = nombre, puntaje

print("\n")
print("****************************************************\n"
      "TABLA DE POSICIONES")
for i in range(10):
    print(tablaPosiciones[i])
print("****************************************************")

os.system("python Menu.py")
