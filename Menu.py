import os

def juego_maribel():
	os.system("clear")
	print("maribel")
	print("juego")

def juego_abi():
	os.system("clear")
	print("abi")
	print("juego")

def juego_julian():
	os.system("clear")
	print("Julian")
	print("juego")

def juego_eloy():
	os.system("clear")
	print("Eloy")
	print("juego")


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
eleccion_menu=int(input("Que juego deseas jugar? >> "))
if eleccion_menu==1:
	juego_maribel()
elif eleccion_menu==2:
        juego_abi()
elif eleccion_menu==3:
        juego_julian()
elif eleccion_menu==4:
        juego_eloy()
elif eleccion_menu==7:
        os.system("exit")
else:
        print("Selecciona una Opcion correcta")
          
