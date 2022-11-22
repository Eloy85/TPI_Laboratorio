Funcion Validacion(r,nivel,puntos)
	Borrar Pantalla
	si r == Verdadero Entonces
		Mostrar "Correcto"
		Mostrar "Pasas el Nivel: " ,nivel
		Mostrar "Tenes ", puntos, " Puntos"
		Leer n
	SiNo si r == Falso entonces
			Borrar Pantalla
			Mostrar "Incorrecto"
			Mostrar "Pasas el Nivel: " ,nivel
			Mostrar "Tenes ", puntos, " Puntos"
			Leer n
		FinSi
	FinSi
FinFuncion

Funcion menu()
	nivel<-0
	puntos<-0
	Borrar Pantalla
	Mostrar ""
	Mostrar "Bienvenido a Fire"
	Mostrar ""
	Mostrar "1) Jugar"
	Mostrar "2) Como Jugar"
	Mostrar "3) Salir"
	Mostrar ""
	Mostrar "Que deseas hacer?"
	Leer eleccion
	si eleccion==1 Entonces
		Level0(nivel,puntos)
	SiNo
		si eleccion==2 Entonces
			como_jugar()
		SiNo
			si eleccion==3
				salir()
			FinSi
		FinSi
	FinSi
FinFuncion
Funcion Level0(nivel,puntos)
	Borrar Pantalla
	Mostrar ""
	Mostrar "Estas en el aula del colegio y sentis una alarma que suena fuerte y muchos gritos afuera"
	Mostrar "depronto una de las otras profes se asoma a tu aula y le dice a tu profesora que hay un incendio en el baño de mujeres"
	Mostrar "tu profesora dice que hagan grupo con otro compañero, se tomen las manos, no se suelten y la sigan afuera"
	Mostrar "Te levantas y no conseguis otro compañero para tomarle la mano."
	Mostrar ""
	Mostrar "Que haces?"
	Mostrar ""
	Mostrar "a) tomas la mano de el primero que encuentras(no importa si tiene compañero)"
	Mostrar "b) Sigues a la profesora solo"
	Leer respuesta
	si respuesta == "a" Entonces
		puntos<-puntos+1
		nivel<-nivel+1
		r<-Verdadero
	SiNo
		puntos<-puntos-1
		nivel<-nivel+1
		r<-Falso
	FinSi
	Validacion(r,nivel,puntos)
	Level1(nivel,puntos,respuesta)
FinFuncion
Funcion Level1(nivel,puntos,respuesta)
		Borrar Pantalla
		Mostrar ""
		Mostrar "Tomaste la mano de un compañero y te dan muchas ganas de ir al baño"
		Mostrar "Tu compañero te dice que no pero si no vas te haras encima."
		Mostrar ""
		Mostrar "Que haces?"
		Mostrar ""
		Mostrar "a) te haces encima pero sigues con tu compañero y el grupo"
		Mostrar "b) Frenas en el baño y haces que tu compañero te espere afuera."
	Leer respuesta
	si respuesta == "a" Entonces
		puntos<-puntos+1
		nivel<-nivel+1
		r<-Verdadero
	SiNo
		puntos<-puntos-1
		nivel<-nivel+1
		r<-Falso
	FinSi
	Validacion(r,nivel,puntos)
	Level2(nivel,puntos,respuesta)
FinFuncion
Funcion Level2(nivel,puntos,respuesta)
	Borrar Pantalla
	Mostrar ""
	Mostrar "Ves todas las puertas cerradas y con un tacho de basura delante de las puertas"
	Mostrar "Detras de una de las puertas se escucha un ruido que no podes distinguir con claridad"
	Mostrar "parece un chico gritando"
	Mostrar ""
	Mostrar "Que haces?"
	Mostrar ""
	Mostrar "a) mal"
	Mostrar "b) bien"
	Leer respuesta
	si respuesta == "b" Entonces
		puntos<-puntos+1
		nivel<-nivel+1
		r<-Verdadero
	SiNo
		puntos<-puntos-1
		nivel<-nivel+1
		r<-Falso
	FinSi
	Validacion(r,nivel,puntos)
	Level3(nivel, puntos,respuesta)
FinFuncion
Funcion Level3(nivel,puntos,respuesta)
	Borrar Pantalla
	Mostrar ""
	Mostrar "Ves una puerta cerrada sin canasto y escuchas un grito de una persona"
	Mostrar ""
	Mostrar "Que haces?"
	Mostrar ""
	Mostrar "a) mal"
	Mostrar "b) Tocar la manija de la puerta y la puerta para ver si esta caliente"
	Leer respuesta
	si respuesta == "b" Entonces
		puntos<-puntos+1
		nivel<-nivel+1
		r<-Verdadero
	SiNo
		puntos<-puntos-1
		nivel<-nivel+1
		r<-Falso
	FinSi
	Validacion(r,nivel,puntos)
	Level4(nivel,puntos,respuesta)
FinFuncion
Funcion Level4(nivel,puntos,respuesta)
	Borrar Pantalla
	Mostrar ""
	Mostrar "Ves la salida pero hay mucho humo en medio y no logras ver ni respirar con facilidad"
	Mostrar ""
	Mostrar "Que haces?"
	Mostrar ""
	Mostrar "a) mal"
	Mostrar "b) Agachate y caminar en cuatro patas poniendo manos y rodillas en el suelo"
	Leer respuesta
	si respuesta == "b" Entonces
		puntos<-puntos+1
		nivel<-nivel+1
		r<-Verdadero
	SiNo
		puntos<-puntos-1
		nivel<-nivel+1
		r<-Falso
	FinSi
	Validacion(r,nivel,puntos)
	Level5(nivel,puntos,respuesta)
FinFuncion
Funcion Level5(nivel,puntos,respuesta)
	Borrar Pantalla
	Mostrar ""
	Mostrar "Te quedas encerrado en la escuela y no hay mas salidas libres que sean seguras"
	Mostrar ""
	Mostrar "Que haces?"
	Mostrar ""
	Mostrar "a) Encerrarte en un cuarto lejos de donde empezo en incendio"
	Mostrar "b) mal"
	Leer respuesta
	si respuesta == "a" Entonces
		puntos<-puntos+1
		nivel<-nivel+1
		r<-Verdadero
	SiNo
		puntos<-puntos-1
		nivel<-nivel+1
		r<-Falso
	FinSi
	Validacion(r,nivel,puntos)
	//	Level5()
FinFuncion

Funcion como_jugar()
	Borrar Pantalla
	Mostrar ""
	Mostrar "El juego es muy simple, se te contara una historia y deberas tomar una desicion entre dos opciones."
	Mostrar "Si es la opcion correcta para sobrevivir se te sumaran puntos y continuaras con la historia presentandote nuevamente dos opciones"
	Mostrar "Si es la opcion incorrecta para sobrevivir pueden pasar 3 cosas dependiendo del nivel de la desision. *Ver los Niveles de las desisiones mas abajo."
	Mostrar "Para elegir entre las opciones solo deberas poner A o B dependiendo la opcion que deseas elegir."
	Mostrar ""
	Mostrar "NOTA: los puntos se califican dependiendo de el nivel de importancia de la desision"
	Mostrar "Nivel de desisiones:"
	Mostrar ""
	Mostrar "Nivel 1:"
	Mostrar "		 Las desisiones de nivel 1 no terminan el juego pero si resta puntos y muestra una advertencia."
	Mostrar "Nivel 2:"
	Mostrar "		 Las desisiones de nivel 2 no terminan el juego pero se resta puntos(mas que nivel 1) y muestra una advertencia."
	Mostrar "Nivel 3:"
	Mostrar "		 Las desisiones de nivel 3 terminan el juego y muestra la cantidad de puntos alcanzados."
	Mostrar ""
	Mostrar "Presiona 1 para volver al menu"
	Leer menu_como_jugar
	si menu_como_jugar==1 Entonces
		menu()
	SiNo
		como_jugar()
	FinSi
FinFuncion
Funcion salir()
FinFuncion

Algoritmo juego_escape
	menu()
FinAlgoritmo

//Funcion respuesta<-jugar2()

//FinFuncion