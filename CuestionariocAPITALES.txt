Algoritmo Cuestionario
	Definir p1, p2, p3, p4, p5 ,p6, p7, p8, p9, p10 Como Caracter
	Definir total, categoria, correctas, incorrectas Como Entero
	total <- 0
	Escribir " Bienvenidos a TalesCapi de America "
	Escribir  " Cual es la capital de Colombia ? "
	escribir "1. Sucre "
	escribir "2. Bogota"
	escribir "3. Caracas"
	escribir " Selecciones la opcion correcta"
	leer p1
	si p1 == "2" Entonces
		total <- total + 10
		correctas <- correctas + 1
	SiNo
		incorrectas <- incorrectas + 1
	FinSi
	escribir " Cual es la capital de Argentina? "
	escribir "1. La plata"
	escribir "2. Buenos Aires"
	escribir "3. Belice"
	escribir " Seleccione la opcion correcta"
	leer p2
	si p2 == "2" Entonces
		total <- total + 10
		correctas <- correctas + 1
	SiNo
		incorrectas <- incorrectas + 1
	FinSi
	escribir " Cual es la capital de Canada ?"
	escribir "1. Ottawa"
	escribir "2. Canada"
	escribir "3. Washington DC"
	escribir " Selecciones la opcion correcta"
	leer p3
	si p3 == "1" Entonces
		total <- total + 10
		correctas <- correctas + 1
	SiNo
		incorrectas <- incorrectas + 1
	FinSi
	escribir " Cual es la capital de Nicaragua"
	escribir "1. Panama"
	escribir "2. Managua"
	escribir "3. Lima"
	escribir " Selecciones la opcion correcta "
	leer p4
	si p4 == "2" Entonces
		total <- total + 10
		correctas <- correctas + 1
	SiNo
		incorrectas <- incorrectas + 1
	FinSi
	escribir " Cual es la capital de Ecuador ?"
	escribir "1. Asuncion"
	escribir "2. Montevideo"
	escribir "3. Quito"
	escribir "Seleccione la opcion correcta"
	leer p5
	si p5 == "3" Entonces
		total <- total + 10
		correctas <- correctas + 1
	SiNo
		incorrectas <- incorrectas + 1
	FinSi
	escribir " Cual es la capital de Trinidad y Tobago ? "
	escribir "1. Parabarimo"
	escribir "2. Sucre"
	escribir "3. Puerto España "
	escribir " Seleccione la opcion correcta"
	leer p6
	si p6 == "3" entonces
		total <- total +10
		correctas <- correctas + 1
	SiNo
		incorrectas <- incorrectas + 1
	FinSi
	escribir " Cual es la capital de Jamaica?"
	escribir "1. Roseau"
	escribir "2. Kingston"
	escribir "3. Puerto Principe"
	escribir "Seleccione la opcion correcta"
	leer p7
	si p7 == "2" Entonces
		total <- total + 10
		correctas <- correctas + 1
	SiNo
		incorrectas <- incorrectas + 1
	FinSi
	escribir " Cual es la capital de Cuba"
	escribir "1. La Habana"
	escribir "2. Georgetown"
	escribir "3. Castries"
	escribir "Seleccione la opcion correcta"
	leer p8
	si p8 == "1" Entonces
		total <- total + 10
		correctas <- correctas + 1
	SiNo
		incorrectas <- incorrectas + 1
	FinSi
	escribir " Cual es la capital de Republica Dominicana"
	escribir "1. Saint John"
	escribir "2. Tegucigalpa"
	escribir "3. Santo Domingo"
	escribir "Seleccione la opcion correcta"
	leer p9
	si p9 == "3" Entonces
		total <- total + 10
		correctas <- correctas + 1
	SiNo
		incorrectas <- incorrectas + 1
	FinSi
	escribir " Cual es la Capital de Estados Unidos?"
	escribir "1. Washington DC"
	escribir "2. Kingstown"
	escribir "3. San Jose"
	escribir "Seleccione la opcion correcta"
	leer p10
	si p10 == "1" Entonces
		total<- total + 10
		correctas <- correctas + 1
	SiNo
		incorrectas <- incorrectas + 1
	FinSi
	escribir " El total del TalesCapi Game es: ", total, "/100"
	si ( total >= 70) Entonces
		escribir " Felicidades"
	sino 	
		escribir " Ups hay que estudiar mas"
	FinSi
	Escribir "Usted tuvo ", correctas, " respuestas correctas y ", incorrectas, " incorrectas"
	
	
FinAlgoritmo
