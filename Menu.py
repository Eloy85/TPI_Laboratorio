import os

def print_menu():
    os.system("clear")
    print("<><><><><><><><><><><><><><><><><><><><>")
    print("<>                                    <>")
    print("<>    Bienvenido a JAME               <>")           
    print("<>    Que queres Aprender Jugando?    <>")
    print("<>    1) Matematicas                  <>")
    print("<>    2) Ingles                       <>")
    print("<>    3) Programacion                 <>")
    print("<>    4)                              <>")
    print("<>    x) Salir                        <>")
    print("<>                                    <>")
    print("<><><><><><><><><><><><><><><><><><><><>")
    print("")

def print_menu_error():
    os.system("clear")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    print("<>                                                                      <>")
    print("<>    Bienvenido a JAME                                                 <>")
    print("<>    Que queres Aprender Jugando?                                      <>")
    print("<>    1) Matematicas                                                    <>")
    print("<>    2) Ingles                                                         <>")
    print("<>    3) Programacion                                                   <>")
    print("<>    4)                                                                <>")
    print("<>    x) Salir                                                          <>")
    print("<>                                                                      <>")
    print("<>    Por favor coloca una opcion valida. Ej: Para Ingles seria: 2      <>")
    print("<>                                                                      <>")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")


def juego_matematicas():
    print_menu()
    print("1")
    programa()

def juego_ingles():
    print_menu()
    print("2")
    programa()

def juego_programacion():
    os.system("clear")
    print("")
    print("Excelente!! Elegiste Programacion!!")
    print("")
    print("")

def juego_cuatro():
    print_menu()
    print("4")
    programa()

def funcion_salir():
    os.system("exit")

def default1():
    print_menu_error()
    programa()

def programa():
    Opcion=input("Elige: ")
    if Opcion=="1":
        juego_matematicas()
    elif Opcion=="2":
        juego_ingles()
    elif Opcion=="3":
        juego_programacion()
    elif Opcion=="4":
        juego_cuatro()
    elif Opcion=="x":
        funcion_salir()
    else:
        default1()

print_menu()
programa()
