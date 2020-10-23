#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    diferencia = numero_1 - numero_2

    if diferencia > 0:
        print("El resultado es Positivo")
    elif diferencia < 0:
        print("El resultado es Negativo")
    else:
        print("El resultado es Cero")


def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    numero_1 = int(input('Ingrese el primer número:\n'))
    if (numero_1 % 2) == 0:
        print("El", numero_1, "Es par")
    else:
        print("El", numero_1, "Es impar")

    numero_2 = int(input('Ingrese el segundo número:\n'))
    if (numero_2 % 2) == 0:
        print("El", numero_2, "Es par")
    else:
        print("El", numero_2, "Es impar")

    numero_3 = int(input('Ingrese el tercer número:\n'))
    if (numero_3 % 2) == 0:
        print("El", numero_3, "Es par")
    else:
        print("El", numero_3, "Es impar")


def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    numero_1 = int(input('Ingrese el primer número:\n'))
    numero_2 = int(input('Ingrese el Segundo número:\n'))

    print("Que operacion desea calcular: + , - , * , / o **:")
    calcular = str(input())

    if calcular == "+":
        print("La suma es", numero_1 + numero_2)
    if calcular == "-":
        print("La resta es", numero_1 - numero_2)
    if calcular == "*":
        print("La multiplicaion es", numero_1 * numero_2)
    if calcular == "/":
        print("La division es", numero_1 / numero_2)
    if calcular == "**":
        print("El exponente es", numero_1 ** numero_2)


def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    palabra_1 = str(input("Ingrese la primera palabra:\n"))
    palabra_2 = str(input("Ingrese la primera palabra:\n"))
    palabra_3 = str(input("Ingrese la primera palabra:\n"))

    longitud_1 = len(palabra_1)
    longitud_2 = len(palabra_2)
    longitud_3 = len(palabra_3)
    
    print("Ingresar 1:(ordenar alfabeticamente) o 2:(Ordenar por cantidad de letras)")
    orden = int(input())

    if orden == 1:
        if (palabra_1 > palabra_2) and (palabra_1 > palabra_3):
            if palabra_2 > palabra_3:
                print("Ordenados Alfabeticamente:", palabra_1, palabra_2, palabra_3)
            else:
                print("Ordenados Alfabeticamente:", palabra_1, palabra_3, palabra_2)
        elif (palabra_2 > palabra_1) and (palabra_2 > palabra_3):
            if palabra_1 > palabra_3:
                print("Ordenados Alfabeticamente:" ,palabra_2, palabra_1, palabra_3)
            else:
                print("Ordenados Alfabeticamente:" ,palabra_2, palabra_3, palabra_1)
        elif (palabra_3 > palabra_1) and (palabra_3 > palabra_2):
            if palabra_3 > palabra_2:
                print("Ordenados Alfabeticamente:" ,palabra_3, palabra_2, palabra_1)
            else:
                print(palabra_3, palabra_1, palabra_2)

    if orden == 2:
        if (longitud_1 > longitud_2) and (longitud_1 > longitud_3):
            if longitud_2 > longitud_3:
                print("Ordenados Por longitud:", longitud_1, longitud_2, longitud_3)
            else:
                print("Ordenados Por longitud:", longitud_1, longitud_3, longitud_2)
        elif (longitud_2 > longitud_1) and (longitud_2 > longitud_3):
            if longitud_1 > longitud_3:
                print("Ordenados Por longitud:" ,longitud_2, longitud_1, longitud_3)
            else:
                print("Ordenados Por longitud:" ,longitud_2, longitud_3, longitud_1)
        elif (longitud_3 > longitud_1) and (longitud_3 > longitud_2):
            if longitud_3 > longitud_2:
                print("Ordenados Por longitud:" ,longitud_3, longitud_2, longitud_1)
            else:
                print(longitud_3, longitud_1, longitud_2)

  







def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    #ej5()
