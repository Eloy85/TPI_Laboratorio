##print("Hola Mundo")     ## Mostrar "Hola Mundo"
##Entrada=input()         ## Leer Entrada
##print(Entrada)          ## Mostrar Entrada
##if Entrada =="1":       ## Si Entrada == "1" Entonces
##    print("Es un uno")  ## Mostrar "Es un uno"
##elif Entrada =="2":     ## Sino si Entrada == "2" Entonces
##    print("Es un dos")  ## Mostrar "Es un dos"
##else:                   ## Sino
##    print("Error")      ## Mostrar "Error"
import os
import random
while True:
    os.system("clear")
    print("")
    print("                                 Bienvenidos a JAME")
    print("")
    print("1) Maribel")
    print("2) Abigail")
    print("3) Julian")
    print("4) Eloy")
    print("5) Indefinido")
    print("6) Contacto")
    print("7) Salir")
    eleccion_menu=int(input())
    if eleccion_menu==1:
        #Juego de Maribel
        print("a")
    elif eleccion_menu==2:
        #Juego de Abigail
        print("a")
    elif eleccion_menu==3:
        #Juego de Julian
        print("a")
    elif eleccion_menu==4:
        #Juego de Eloy
        print("a")
    elif eleccion_menu==7:
        break
    else:
        print("Selecciona una Opcion correcta")
        
        
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

