import os

print("<><><><><><><><><><><><><><><><><><><><>\n"
      "<>                                    <>\n"
      "<>    Bienvenido/a!                   <>\n"
      "<>    ¿Qué quieres aprender jugando?  <>\n"
      "<>    1) MateMata                     <>\n"
      "<>    2) TalesCapi                    <>\n"
      "<>    x) Salir                        <>\n"
      "<>                                    <>\n"
      "<><><><><><><><><><><><><><><><><><><><>\n"
      "\n")

opcion = input("Elige: ")
if opcion == "1":
    os.system("python MateMata.py")
elif opcion == "2":
    os.system("python TalesCapi.py")
elif opcion == "x":
    os.system("exit")

while opcion != "1" and opcion != "2" and opcion != "x":
    print("<><><><><><><><><><><><><><><><><><><><>\n"
          "<>                                    <>\n"
          "<>    Bienvenido/a!                   <>\n"
          "<>    ¿Qué quieres aprender jugando?  <>\n"
          "<>    1) MateMata                     <>\n"
          "<>    2) TalesCapi                    <>\n"
          "<>    x) Salir                        <>\n"
          "<>                                    <>\n"
          "<> Por favor coloca una opción válida.<>\n"
          "<> Ej.: Para TalesCapi ingresa: 2     <>\n"
          "<><><><><><><><><><><><><><><><><><><><>\n"
          "\n")
    opcion = input("Elige: ")
    if opcion == "1":
        os.system("python MateMata.py")
    elif opcion == "2":
        os.system("python TalesCapi.py")
    elif opcion == "x":
        os.system("exit")
