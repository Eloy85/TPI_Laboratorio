Algoritmo MateMata
	Definir tipoOperacion, i, a, b, resultado, puntaje Como Entero
	Definir salir Como Caracter
	Repetir
		Escribir "¡Bienvenido a MateMata! Elige una categoría"
		Escribir "1 - SUMA"
		Escribir "2 - RESTA"
		Escribir "3 - MULTIPLICACION"
		Escribir "4 - DIVISION"
		Escribir "Ingresa la opción elegida (1 - 4)"
		Leer tipoOperacion
		Mientras tipoOperacion > 4 o tipoOperacion < 1 Hacer
			Escribir "Opción incorrecta. Ingresa la opción elegida (1 - 4)"
			Leer tipoOperacion
		FinMientras
		Escribir "Seleccione el nivel de dificultad (1 - 3)"
		Escribir "1 - Fácil"
		Escribir "2 - Medio"
		Escribir "3 - Difícil"
		Leer nivel
		Mientras nivel > 3 o nivel < 1 Hacer
			Escribir "Opción incorrecta. Seleccione el nivel de dificultad (1 - 3)"
			Leer nivel
		FinMientras
		Segun tipoOperacion Hacer
			1: //suma
				i = 0
				Para i=1 Hasta 10 Hacer				
					Segun nivel Hacer
						1:
							a = Aleatorio(1, 9)
							b = Aleatorio(1, 9)
						2:
							a = Aleatorio(1, 99)
							b = Aleatorio(1, 99)
						3:
							a = Aleatorio(1, 999)
							b = Aleatorio(1, 999)
					FinSegun
					Escribir "*** Pregunta ", i, " de 10 ***"
					Escribir a, " + ", b, " ="
					Leer resultado
					Si resultado = a+b Entonces
						Segun nivel Hacer
							1:
								puntaje = puntaje + 10
								Escribir "¡Correcto! Sumás 10 puntos"
							2:
								puntaje = puntaje + 20
								Escribir "¡Correcto! Sumás 20 puntos"
							3:
								puntaje = puntaje + 30
								Escribir "¡Correcto! Sumás 30 puntos"
						FinSegun
					SiNo
						Escribir "Incorrecto. La respuesta correcta es ", a+b
					FinSi
				FinPara
				Escribir "Fin de la ronda. Tu puntaje total es ", puntaje
			2: //resta
				i = 0
				Para i=1 Hasta 10 Hacer
					Segun nivel Hacer
						1:
							a = Aleatorio(1, 9)
							b = Aleatorio(1, 9)
						2:
							a = Aleatorio(1, 99)
							b = Aleatorio(1, 99)
						3:
							a = Aleatorio(1, 999)
							b = Aleatorio(1, 999)
					FinSegun
					Mientras a<b Hacer
						Segun nivel Hacer
							1:
								a = Aleatorio(1, 9)
								b = Aleatorio(1, 9)
							2:
								a = Aleatorio(1, 99)
								b = Aleatorio(1, 99)
							3:
								a = Aleatorio(1, 999)
								b = Aleatorio(1, 999)
						FinSegun
					FinMientras
					Escribir "*** Pregunta ", i, " de 10 ***"
					Escribir a, " - ", b, " ="
					Leer resultado
					Si resultado = a-b Entonces
						Segun nivel Hacer
							1:
								puntaje = puntaje + 10
								Escribir "¡Correcto! Sumás 10 puntos"
							2:
								puntaje = puntaje + 20
								Escribir "¡Correcto! Sumás 20 puntos"
							3:
								puntaje = puntaje + 30
								Escribir "¡Correcto! Sumás 30 puntos"
						FinSegun
					SiNo
						Escribir "Incorrecto. La respuesta correcta es ", a-b
					FinSi
				FinPara
				Escribir "Fin de la ronda. Tu puntaje total es ", puntaje
			3: //multiplicacion
				i = 0
				Para i=1 Hasta 10 Hacer				
					Segun nivel Hacer
						1:
							a = Aleatorio(1, 9)
							b = Aleatorio(1, 9)
						2:
							a = Aleatorio(1, 99)
							b = Aleatorio(1, 99)
						3:
							a = Aleatorio(1, 999)
							b = Aleatorio(1, 999)
					FinSegun
					Escribir "*** Pregunta ", i, " de 10 ***"
					Escribir a, " x ", b, " ="
					Leer resultado
					Si resultado = a*b Entonces
						Segun nivel Hacer
							1:
								puntaje = puntaje + 10
								Escribir "¡Correcto! Sumás 10 puntos"
							2:
								puntaje = puntaje + 20
								Escribir "¡Correcto! Sumás 20 puntos"
							3:
								puntaje = puntaje + 30
								Escribir "¡Correcto! Sumás 30 puntos"
						FinSegun
					SiNo
						Escribir "Incorrecto. La respuesta correcta es ", a*b
					FinSi
				FinPara
				Escribir "Fin de la ronda. Tu puntaje total es ", puntaje
			4: //division
				i = 0
				Para i=1 Hasta 10 Hacer
					Segun nivel Hacer
						1:
							a = Aleatorio(1, 9)
							b = Aleatorio(1, 9)
						2:
							a = Aleatorio(1, 99)
							b = Aleatorio(1, 99)
						3:
							a = Aleatorio(1, 999)
							b = Aleatorio(1, 999)
					FinSegun
					Mientras a%b<>0 Hacer
						Segun nivel Hacer
							1:
								a = Aleatorio(1, 9)
								b = Aleatorio(1, 9)
							2:
								a = Aleatorio(1, 99)
								b = Aleatorio(1, 99)
							3:
								a = Aleatorio(1, 999)
								b = Aleatorio(1, 999)
						FinSegun
					FinMientras
					Escribir "*** Pregunta ", i, " de 10 ***"
					Escribir a, " / ", b, " ="
					Leer resultado
					Si resultado = a/b Entonces
						Segun nivel Hacer
							1:
								puntaje = puntaje + 10
								Escribir "¡Correcto! Sumás 10 puntos"
							2:
								puntaje = puntaje + 20
								Escribir "¡Correcto! Sumás 20 puntos"
							3:
								puntaje = puntaje + 30
								Escribir "¡Correcto! Sumás 30 puntos"
						FinSegun
					SiNo
						Escribir "Incorrecto. La respuesta correcta es ", a/b
					FinSi
				FinPara
				Escribir "Fin de la ronda. Tu puntaje total es ", puntaje
		FinSegun
		Escribir "¿Desea volver a jugar? S/N"
		Leer salir
		Mientras (Mayusculas(salir) <> "S") y (Mayusculas(salir) <> "N") Hacer
			Escribir "¿Desea volver a jugar? S/N"
			Leer salir
		FinMientras
	Hasta Que Mayusculas(salir) = "N"
FinAlgoritmo
