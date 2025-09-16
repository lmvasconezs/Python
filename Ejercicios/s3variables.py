# Como defino un objeto dentro de python?
#Tengo que declarar una variable y darle un valor
# El numero 5 es el que va a ser el objeto
# Cuando no defino si es de tipo float o no defino especificamente una varible automaticamente Python me va a tomar como un tipo Int, como un tipo entero
# x va a ser la variable que hace referencia a ese objeto
x=5


# Aqui con la doble comilla estoy definiendo el string Juan, y este va a ser el objeto de la clase
# Python lo que hace internamente es definir esta cadena de texto como str
# Y el metodo upper va a ser un comportamiento o metodo definido para esa clase para poder convertir todas las letras en mayusculas
nombre="Juan" # Aqui defino una cadena de texto de tipo STRING
print(nombre.upper())

#Variable de tipo entero
edad=23

#Boolean
es_estudiante=True


# Variable de tipo decimal o flotante: Se puede definir como tal ya el valor flotante o pedirle al usuario que me ingrese un valor y este sea de tipo flotante
altura=1.75 # Aqui automaticamente estoy asignandole a mi variable un valor flotante al usar el PUNTO

print(nombre, edad, altura, es_estudiante)

## Variables con valores numericos para operaciones matematicas
x=10
y=5

suma = x+y
resta = x-y
producto = x*y
division = x/y

print(suma, resta, producto, division)
print("Suma: ", suma)
print("Resta: ", resta)
print("Producto: ", producto)
print("Division: ", division)

operacion= (2+3)*4**2/2-5
print(operacion) ## De esta forma, sacando el resultado por medio de una variable, se usa mas memoria, porque el valor queda guardado mientras el programa siga en ejecucion. Es util cuando vamos a usar el valor varias veces

## IMPORTANTE seguir la jerarquia. Primero parentesis, potencia, division, multiplicacion, suma y resta

print((2+3)*4**2/2-5) ## De esta forma se optimizan mas los recursos de la computadora, se usa menos memoria, usando el print directo, porque solo calcula y muestra el valor, sin guardarlo

# Pero si necesitamos usar el resultado una y otra vez, tendra que ser recalculado
## En conclusion, si se quiere ahorrar memoria, hay que imprimir el calculo directo
## Pero si queremos reutilizar el valor, hay que guardarlo en una varible, aunque ocupe un poco mas de memoria

