import os
import random

os.system("clear")
print("")
print(" APRENDEMOS LOS NUMEROS PAR E IMPAR ")
print(" 1) Jugar")
print(" 2) Reglas del juego")
print(" 3) Salir")
ele_menu=int(input())
if ele_menu==1:
	os.system("clear")
	while True:
		while True:
			A=random.randint(0,99)
			if A%2==0:
				print ("Escribe 100 para salir")
				print (A)
				break
		while True:
			B=random.randint(0,99)
			if B%2!=0:
				print(B)
				break
		eleccion=int(input("¿cual es el numero par? >> "))
		if eleccion==A:
			print("correcto")
			input("Presiona enter para continuar")
			os.system("clear")
		elif eleccion==B:
			print(" no coincide con la pregunta pero es impar")
			input("Presiona enter para continuar")
			os.system("clear")
		elif eleccion==100:
			break
		else:
			print("vuelve a jugar y elige bien la opcion")
			print("")
			input("Presiona enter para continuar")
			os.system("clear")
elif ele_menu==2:
	print("REGLAS DEL JUEGO")
	print("un numero par lo podemos identificar ya que si lo dividimos por 2 y su resto da 0")
	print("un numero par tambien lo podemos identificar cuando termina en: 0, 2, 4, 6 u 8") 
	print("un numero impar lo podemos identificar ya que si lo dividimos por 2 y su resto es diferente a 0")
	print("un numero impar tambien lo podemos identificar cuando termina en : 1, 3, 5, 7, 9")
else:
	os.system("exit")
