print("Hola Mundo")
## Ejercicio 1: Hay que generar un programa que genere un promedio de 3 notas. No me esta indicando que le pida al usuario que de las notas, por lo que puedo hacerlo de 2 formas, dejando quemadas las 3 notas, o pedirle al usuario las notas
## Lo primero que voy a hacer es solicitarle al usuario las 3 notas

print("Bienvenido al calculo de promedio")
## Primero voy a definir una variable
nota1=float(input("Ingresa la primera nota: "))
## Ojo, tengo que colocar de que tipo es la variable antes del input, asi que como va a ser un numero que puede tener decimales, uso float, que me va a permitir ingresar una nota entera o decimal
# Uso input para solicitar texto, para poder responderle


nota2=float(input("Ingresa la segunda nota: "))
nota3=float(input("Ingresa la tercera nota: "))

## Ahora, para promediar tengo que hacer que su sumen las 3 notas y se divindan para 3
## Empiezo definiendo la variable que va a contener este resultado, que a su vez va a definir el proceso que quiero desarrollar

promedio=(nota1+nota2+nota3)/3
## Si dejo esto asi, me va a dar un error semantico (ya que no va cumplir el objetivo que yo quiero) pq va a dividir la nota 3 para 3 nomas
## Ademas, no se me va a imprimir la respuesta
promedio=print((nota1+nota2+nota3)/3)


## Ejercicio 2: Concatenar nombre y apellido para mostrar el nombre completo
print("Nombre completo")
nombre=input("Ingrese el nombre: ")
apellido=input("Ingrese su apellido: ")
nombrecompleto=nombre +" "+ apellido
##Pongo las dos comillas entre nombre y apellido para que se deje un espacio
print("Tu nombre completo es: ", nombrecompleto)
## Ojo que separo el texto que se va a imprimir de la respuesta de la variable con una coma

##Ejercicio 3: Vamos a ingresar una frase y vamos a programar el texto a todo mayuscula y que me cuente cuantas letras tiene esa frase
# Para transformar todo a mayuscula usamos la funcion upper
# Y para contar usamos la funcion len
print("Bienvenido al programa de manejo de texto")
frase=input("Ingrese la frase: ")

#Desarrollo del proceso
frasemayuscula=frase.upper()
print(frasemayuscula)
cantidadfrase=len(frasemayuscula)
print(cantidadfrase)


## Count se usa para contar cuantas veces aparece un valor dentro de una cadena de texto
frase=("Programar en Python es divertido y Python es popular")
conteo=frase.count("Python")
print("La palabra 'Python' aparece:", conteo, "veces")
