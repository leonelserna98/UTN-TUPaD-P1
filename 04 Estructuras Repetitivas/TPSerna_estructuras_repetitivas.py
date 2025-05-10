#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tecnicatura Universitaria en Programación a Distancia
Práctico 4: Estructuras repetitivas
Serna Leonel

Este programa implementa los 10 ejercicios del práctico sobre estructuras
repetitivas utilizando ciclos para resolver problemas que requieren repetición
de acciones.
"""
import random  # Importamos random para el ejercicio 5

def ejercicio1():
    """
    Imprime en pantalla todos los números enteros desde 0 hasta 100
    (incluyendo ambos extremos), en orden creciente.
    """
    print("\n=== Ejercicio 1 ===")
    print("Imprimiendo números del 0 al 100:")
    
    # Utilizamos un bucle for para iterar del 0 al 100 inclusive
    for numero in range(0, 101):
        print(numero)
    
    print("Fin del ejercicio 1")

def ejercicio2():
    """
    Solicita al usuario un número entero y determina la cantidad de dígitos
    que contiene.
    """
    print("\n=== Ejercicio 2 ===")
    
    # Solicitamos y validamos el número
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    # Convertimos a valor absoluto para contar dígitos (para incluir negativos)
    numero_abs = abs(numero)
    
    # Método 1: Convertir a string y contar caracteres
    cantidad_digitos = len(str(numero_abs))
    
    # Método 2: Método matemático (descomentar para usar)
    # cantidad_digitos = 1  # Todo número tiene al menos 1 dígito
    # while numero_abs >= 10:
    #     numero_abs //= 10
    #     cantidad_digitos += 1
    
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
    print("Fin del ejercicio 2")

def ejercicio3():
    """
    Suma todos los números enteros comprendidos entre dos valores dados
    por el usuario, excluyendo esos dos valores.
    """
    print("\n=== Ejercicio 3 ===")
    
    # Solicitamos los dos valores
    while True:
        try:
            valor1 = int(input("Ingrese el primer valor entero: "))
            valor2 = int(input("Ingrese el segundo valor entero: "))
            break
        except ValueError:
            print("Debe ingresar valores enteros válidos.")
    
    # Aseguramos que valor1 sea menor que valor2
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1  # Intercambiamos valores
    
    # Calculamos la suma de los números entre los valores (excluyendo ambos)
    suma = 0
    for numero in range(valor1 + 1, valor2):
        suma += numero
    
    print(f"La suma de los números entre {valor1} y {valor2} (sin incluirlos) es: {suma}")
    print("Fin del ejercicio 3")

def ejercicio4():
    """
    Permite al usuario ingresar números enteros y los suma en secuencia.
    El programa se detiene y muestra el total acumulado cuando el usuario
    ingresa un 0.
    """
    print("\n=== Ejercicio 4 ===")
    print("Ingrese números enteros para sumarlos (ingrese 0 para terminar):")
    
    suma = 0
    while True:
        try:
            numero = int(input("Ingrese un número (0 para terminar): "))
            
            # Verificamos si es momento de terminar
            if numero == 0:
                break
                
            # Sumamos el número ingresado
            suma += numero
            
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    print(f"La suma total de los números ingresados es: {suma}")
    print("Fin del ejercicio 4")

def ejercicio5():
    """
    Juego en el que el usuario debe adivinar un número aleatorio entre 0 y 9.
    Al final, muestra cuántos intentos fueron necesarios para acertar el número.
    """
    print("\n=== Ejercicio 5 ===")
    print("Adivina un número entre 0 y 9")
    
    # Generamos un número aleatorio entre 0 y 9
    numero_secreto = random.randint(0, 9)
    intentos = 0
    
    while True:
        try:
            intento = int(input("Ingrese su intento: "))
            intentos += 1
            
            # Validamos el rango
            if intento < 0 or intento > 9:
                print("El número debe estar entre 0 y 9. Intente nuevamente.")
                continue
            
            # Verificamos si adivinó
            if intento == numero_secreto:
                print(f"¡Correcto! El número era {numero_secreto}.")
                print(f"Lo adivinaste en {intentos} intentos.")
                break
            elif intento < numero_secreto:
                print("El número es mayor. Intenta nuevamente.")
            else:
                print("El número es menor. Intenta nuevamente.")
                
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    print("Fin del ejercicio 5")

def ejercicio6():
    """
    Imprime en pantalla todos los números pares comprendidos entre 0 y 100,
    en orden decreciente.
    """
    print("\n=== Ejercicio 6 ===")
    print("Números pares entre 0 y 100 en orden decreciente:")
    
    # Iteramos en orden decreciente desde 100 hasta 0 de 2 en 2
    for numero in range(100, -1, -2):
        print(numero)
    
    print("Fin del ejercicio 6")

def ejercicio7():
    """
    Calcula la suma de todos los números comprendidos entre 0 y un número
    entero positivo indicado por el usuario.
    """
    print("\n=== Ejercicio 7 ===")
    
    # Solicitamos y validamos el número
    while True:
        try:
            limite = int(input("Ingrese un número entero positivo: "))
            if limite <= 0:
                print("Debe ingresar un número positivo.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    # Calculamos la suma
    suma = 0
    for numero in range(0, limite + 1):
        suma += numero
    
    # Alternativa más eficiente usando la fórmula matemática
    # suma = (limite * (limite + 1)) // 2
    
    print(f"La suma de los números entre 0 y {limite} es: {suma}")
    print("Fin del ejercicio 7")

def ejercicio8():
    """
    Permite al usuario ingresar 100 números enteros e indica cuántos son pares,
    impares, negativos y positivos.
    Para facilitar las pruebas, usaremos una cantidad más pequeña pero el programa
    está preparado para 100 números.
    """
    print("\n=== Ejercicio 8 ===")
    
    # Definimos la cantidad de números a procesar
    cantidad_numeros = 100
    
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    ceros = 0
    
    print(f"Ingrese {cantidad_numeros} números enteros:")
    
    for i in range(cantidad_numeros):
        while True:
            try:
                numero = int(input(f"Número {i+1}/{cantidad_numeros}: "))
                break
            except ValueError:
                print("Debe ingresar un número entero válido.")
        
        # Verificamos si es par o impar
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        # Verificamos si es positivo, negativo o cero
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1
    
    print("\nResultados:")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")
    print(f"Ceros: {ceros}")
    print("Fin del ejercicio 8")

def ejercicio9():
    """
    Permite al usuario ingresar 100 números enteros y calcula la media de esos valores.
    Para facilitar las pruebas, usaremos una cantidad más pequeña pero el programa
    está preparado para 100 números.
    """
    print("\n=== Ejercicio 9 ===")
    
    # Definimos la cantidad de números a procesar (cambiar a 100 para la versión final)
    cantidad_numeros = 5  # Para pruebas usamos 5, pero debe ser 100 para la entrega
    
    suma = 0
    
    print(f"Ingrese {cantidad_numeros} números enteros:")
    
    for i in range(cantidad_numeros):
        while True:
            try:
                numero = int(input(f"Número {i+1}/{cantidad_numeros}: "))
                break
            except ValueError:
                print("Debe ingresar un número entero válido.")
        
        suma += numero
    
    # Calculamos la media
    media = suma / cantidad_numeros
    
    print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")
    print("Fin del ejercicio 9")

def ejercicio10():
    """
    Invierte el orden de los dígitos de un número ingresado por el usuario.
    Ejemplo: 547 -> 745
    """
    print("\n=== Ejercicio 10 ===")
    
    # Solicitamos y validamos el número
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("Debe ingresar un número entero válido.")
    
    # Manejamos el caso de números negativos
    es_negativo = numero < 0
    numero_abs = abs(numero)
    
    # Método 1: Usando strings
    numero_invertido_str = str(numero_abs)[::-1]
    numero_invertido = int(numero_invertido_str)
    
    # Método 2: Método matemático (descomentar para usar)
    # numero_invertido = 0
    # temp = numero_abs
    # while temp > 0:
    #     digito = temp % 10
    #     numero_invertido = numero_invertido * 10 + digito
    #     temp //= 10
    
    # Si el número original era negativo, el invertido también debe serlo
    if es_negativo:
        numero_invertido = -numero_invertido
    
    print(f"El número {numero} invertido es: {numero_invertido}")
    print("Fin del ejercicio 10")

def menu():
    """
    Muestra un menú para que el usuario seleccione qué ejercicio ejecutar.
    """
    while True:
        print("\n========================================")
        print("PRÁCTICO 4: ESTRUCTURAS REPETITIVAS")
        print("========================================")
        print("1. Imprimir números del 0 al 100")
        print("2. Contar dígitos de un número")
        print("3. Sumar números entre dos valores")
        print("4. Sumar números hasta ingresar 0")
        print("5. Adivinar número aleatorio")
        print("6. Imprimir pares de 100 a 0")
        print("7. Suma de números de 0 a N")
        print("8. Contar pares, impares, positivos y negativos")
        print("9. Calcular media de números")
        print("10. Invertir dígitos de un número")
        print("0. Salir")
        
        try:
            opcion = int(input("\nSeleccione un ejercicio (0-10): "))
            
            if opcion == 0:
                print("¡Gracias por utilizar el programa!")
                break
            elif opcion == 1:
                ejercicio1()
            elif opcion == 2:
                ejercicio2()
            elif opcion == 3:
                ejercicio3()
            elif opcion == 4:
                ejercicio4()
            elif opcion == 5:
                ejercicio5()
            elif opcion == 6:
                ejercicio6()
            elif opcion == 7:
                ejercicio7()
            elif opcion == 8:
                ejercicio8()
            elif opcion == 9:
                ejercicio9()
            elif opcion == 10:
                ejercicio10()
            else:
                print("Opción no válida. Intente nuevamente.")
                
            input("\nPresione Enter para continuar...")
            
        except ValueError:
            print("Debe ingresar un número entero válido.")

# Punto de entrada del programa
if __name__ == "__main__":
    print("Bienvenido al Práctico 4 de Estructuras Repetitivas")
    menu()
