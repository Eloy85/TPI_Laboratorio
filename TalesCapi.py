import os
salir = str()

while salir != "n":
	total = 0
	correctas = 0
	incorrectas = 0
	print(" Bienvenidos a TalesCapi de America\n"
		  "Cual es la capital de Colombia?\n"
		  "1. Sucre\n"
		  "2. Bogota\n"
		  "3. Caracas\n"
		  "Seleccione la opcion correcta")
	p1 = int(input())
	if p1 == 2:
		total += 10
		correctas += 1
	else:
		incorrectas += 1

	print("Cual es la capital de Argentina?\n"
		  "1. La plata\n"
		  "2. Buenos Aires\n"
		  "3. Belice\n"
		  "Seleccione la opcion correcta")
	p2 = int(input())
	if p2 == 2:
		total += 10
		correctas += 1
	else:
		incorrectas += 1

	print(" Cual es la capital de Canada?\n"
		  "1. Ottawa\n"
		  "2. Canada\n"
		  "3. Washington DC\n"
		  "Seleccione la opcion correcta")
	p3 = int(input())
	if p3 == 1:
		total += 10
		correctas += 1
	else:
		incorrectas += 1

	print("Cual es la capital de Nicaragua\n"
		  "1. Panama\n"
		  "2. Managua\n"
		  "3. Lima\n"
		  "Seleccione la opcion correcta")
	p4 = int(input())
	if p4 == 2:
		total += 10
		correctas += 1
	else:
		incorrectas += 1

	print("Cual es la capital de Ecuador?\n"
		  "1. Asuncion\n"
		  "2. Montevideo\n"
		  "3. Quito\n"
		  "Seleccione la opcion correcta")
	p5 = int(input())
	if p5 == 3:
		total += 10
		correctas += 1
	else:
		incorrectas += 1

	print("Cual es la capital de Trinidad y Tobago?\n"
		  "1. Parabarimo\n"
		  "2. Sucre\n"
		  "3. Puerto España\n"
		  "Seleccione la opcion correcta")
	p6 = int(input())
	if p6 == 3:
		total += 10
		correctas += 1
	else:
		incorrectas += 1

	print("Cual es la capital de Jamaica?\n"
		  "1. Roseau\n"
		  "2. Kingston\n"
		  "3. Puerto Principe\n"
		  "Seleccione la opcion correcta")
	p7 = int(input())
	if p7 == 2:
		total += 10
		correctas += 1
	else:
		incorrectas += 1

	print("Cual es la capital de Cuba?\n"
		  "1. La Habana\n"
		  "2. Georgetown\n"
		  "3. Castries\n"
		  "Seleccione la opcion correcta")
	p8 = int(input())
	if p8 == 1:
		total += 10
		correctas += 1
	else:
		incorrectas += 1

	print("Cual es la capital de Republica Dominicana?\n"
		  "1. Saint John\n"
		  "2. Tegucigalpa\n"
		  "3. Santo Domingo\n"
		  "Seleccione la opcion correcta")
	p9 = int(input())
	if p9 == 3:
		total += 10
		correctas += 1
	else:
		incorrectas += 1

	print("Cual es la Capital de Estados Unidos?\n"
		  "1. Washington DC\n"
		  "2. Kingstown\n"
		  "3. San Jose\n"
		  "Seleccione la opcion correcta")
	p10 = int(input())
	if p10 == 1:
		total += 10
		correctas += 1
	else:
		incorrectas += 1

	print(f"El total del TalesCapi Game es {total}/100")
	if total >= 70:
		print("Felicidades!")
	else:
		print("Ups hay que estudiar mas")
	print(f"Usted tuvo {correctas} respuestas correctas y {incorrectas} incorrectas")

	salir = str(input("¿Desea volver a jugar? S/N): "))
	while salir != "s" and salir != "n":
		salir = str(input("¿Desea volver a jugar? S/N): "))

os.system("python Menu.py")
