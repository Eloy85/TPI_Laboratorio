Funcion menu()
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
		jugar()
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
Funcion jugar()
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
