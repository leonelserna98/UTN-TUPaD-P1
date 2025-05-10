
"""
Tecnicatura Universitaria en Programación a Distancia
Práctico 5: Listas
Serna Leonel

Este programa implementa los 10 ejercicios del práctico sobre listas en Python,
aplicando conceptos como indexación, modificación de elementos, uso de métodos
integrados y manejo de listas anidadas.
"""

def ejercicio1():
    """
    Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
    Utilizar la función range.
    """
    print("\n=== Ejercicio 1 ===")
    
    # Creamos una lista con los múltiplos de 4 del 1 al 100
    # Para esto, comenzamos en 4 y saltamos de 4 en 4 hasta llegar a 100 (incluido)
    multiplos_de_4 = list(range(4, 101, 4))
    
    print("Lista de múltiplos de 4 del 1 al 100:")
    print(multiplos_de_4)
    
    # También podríamos usar comprensión de listas
    # multiplos_de_4 = [num for num in range(1, 101) if num % 4 == 0]
    
    print("Fin del ejercicio 1")

def ejercicio2():
    """
    Crear una lista con cinco elementos y mostrar el penúltimo.
    """
    print("\n=== Ejercicio 2 ===")
    
    # Creamos una lista con 5 elementos
    mis_elementos = ["Python", "Java", "C++", "JavaScript", "Ruby"]
    
    # Mostramos la lista completa
    print("Lista completa:", mis_elementos)
    
    # Mostramos el penúltimo elemento usando indexación positiva
    print("Penúltimo elemento (usando indexación positiva):", mis_elementos[3])
    
    # Mostramos el penúltimo elemento usando indexación negativa
    # El índice -1 accede al último elemento, -2 al penúltimo, etc.
    print("Penúltimo elemento (usando indexación negativa):", mis_elementos[-2])
    
    print("Fin del ejercicio 2")

def ejercicio3():
    """
    Crear una lista vacía, agregar tres palabras con append e imprimir
    la lista resultante por pantalla.
    """
    print("\n=== Ejercicio 3 ===")
    
    # Creamos una lista vacía
    lista_vacia = []
    print("Lista inicial vacía:", lista_vacia)
    
    # Agregamos tres palabras con append
    lista_vacia.append("Programación")
    lista_vacia.append("Python")
    lista_vacia.append("Listas")
    
    # Imprimimos la lista resultante
    print("Lista después de agregar elementos:", lista_vacia)
    
    print("Fin del ejercicio 3")

def ejercicio4():
    """
    Reemplazar el segundo y último valor de la lista "animales" con las palabras
    "loro" y "oso", respectivamente. Imprimir la lista resultante por pantalla.
    """
    print("\n=== Ejercicio 4 ===")
    
    # Lista de animales inicial
    animales = ["perro", "gato", "conejo", "pez"]
    print("Lista de animales inicial:", animales)
    
    # Reemplazamos el segundo valor (índice 1) por "loro"
    animales[1] = "loro"
    
    # Reemplazamos el último valor usando indexación negativa
    animales[-1] = "oso"
    
    # Imprimimos la lista resultante
    print("Lista de animales después de reemplazar:", animales)
    
    print("Fin del ejercicio 4")

def ejercicio5():
    """
    Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
    
    numeros = [8, 15, 3, 22, 7]
    numeros.remove(max(numeros))
    print(numeros)
    """
    print("\n=== Ejercicio 5 ===")
    
    # Código a analizar
    print("Código a analizar:")
    print("numeros = [8, 15, 3, 22, 7]")
    print("numeros.remove(max(numeros))")
    print("print(numeros)")
    
    print("\nEjecución del código:")
    numeros = [8, 15, 3, 22, 7]
    print("Lista original:", numeros)
    
    # Identificamos el valor máximo
    valor_maximo = max(numeros)
    print(f"Valor máximo en la lista: {valor_maximo}")
    
    # Eliminamos el valor máximo
    numeros.remove(valor_maximo)
    print("Lista después de eliminar el valor máximo:", numeros)
    
    # Explicación del código:
    print("\nExplicación del código:")
    print("1. Se crea una lista llamada 'numeros' con 5 valores enteros: 8, 15, 3, 22 y 7.")
    print("2. Se utiliza la función 'max(numeros)' para encontrar el valor máximo de la lista, que es 22.")
    print("3. Se utiliza el método 'remove()' para eliminar la primera ocurrencia del valor máximo (22) de la lista.")
    print("4. Finalmente, se imprime la lista actualizada sin el valor máximo.")
    print("5. El resultado es la lista original sin el número más grande: [8, 15, 3, 7].")
    
    print("En resumen, este código encuentra y elimina el número más grande de una lista.")
    
    print("\nFin del ejercicio 5")

def ejercicio6():
    """
    Crear una lista con números del 10 al 30 (incluido), haciendo saltos de 5 en 5
    y mostrar por pantalla los dos primeros.
    """
    print("\n=== Ejercicio 6 ===")
    
    # Creamos la lista con números del 10 al 30 (incluido) con saltos de 5
    numeros = list(range(10, 31, 5))
    
    # Mostramos la lista completa
    print("Lista completa:", numeros)
    
    # Mostramos los dos primeros elementos
    print("Los dos primeros elementos son:", numeros[:2])
    print("Primer elemento:", numeros[0])
    print("Segundo elemento:", numeros[1])
    
    print("Fin del ejercicio 6")

def ejercicio7():
    """
    Reemplazar los dos valores centrales (índices 1 y 2) de la lista "autos"
    por dos nuevos valores cualesquiera.
    """
    print("\n=== Ejercicio 7 ===")
    
    # Lista de autos inicial
    autos = ["sedan", "polo", "suran", "gol"]
    print("Lista de autos inicial:", autos)
    
    # Reemplazamos los dos valores centrales (índices 1 y 2)
    autos[1] = "toyota"
    autos[2] = "bmw"
    
    # Imprimimos la lista resultante
    print("Lista de autos después de reemplazar:", autos)
    
    print("Fin del ejercicio 7")

def ejercicio8():
    """
    Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15
    usando append directamente. Imprimir la lista resultante por pantalla.
    """
    print("\n=== Ejercicio 8 ===")
    
    # Creamos una lista vacía llamada "dobles"
    dobles = []
    print("Lista vacía inicial:", dobles)
    
    # Agregamos el doble de 5, 10 y 15 usando append directamente
    dobles.append(5 * 2)  # Doble de 5
    dobles.append(10 * 2)  # Doble de 10
    dobles.append(15 * 2)  # Doble de 15
    
    # Imprimimos la lista resultante
    print("Lista con los dobles de 5, 10 y 15:", dobles)
    
    print("Fin del ejercicio 8")

def ejercicio9():
    """
    Dada la lista "compras", cuyos elementos representan los productos comprados
    por diferentes clientes:
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    
    a) Agregar "jugo" a la lista del tercer cliente usando append.
    b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    c) Eliminar "pan" de la lista del primer cliente.
    d) Imprimir la lista resultante por pantalla
    """
    print("\n=== Ejercicio 9 ===")
    
    # Lista de compras inicial
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    print("Lista de compras inicial:", compras)
    
    # a) Agregar "jugo" a la lista del tercer cliente
    compras[2].append("jugo")
    print("Después de agregar 'jugo' al tercer cliente:", compras)
    
    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
    # Primero encontramos el índice de "fideos" en la lista del segundo cliente
    indice_fideos = compras[1].index("fideos")
    # Luego reemplazamos el valor en ese índice
    compras[1][indice_fideos] = "tallarines"
    print("Después de reemplazar 'fideos' por 'tallarines':", compras)
    
    # c) Eliminar "pan" de la lista del primer cliente
    compras[0].remove("pan")
    print("Después de eliminar 'pan' del primer cliente:", compras)
    
    # d) Imprimimos la lista resultante
    print("Lista de compras final:", compras)
    
    print("Fin del ejercicio 9")

def ejercicio10():
    """
    Elaborar una lista anidada llamada "lista_anidada" que contenga los
    siguientes elementos:
    ● Posición lista_anidada[0]: 15
    ● Posición lista_anidada[1]: True
    ● Posición lista_anidada[2][0]: 25.5
    ● Posición lista_anidada[2][1]: 57.9
    ● Posición lista_anidada[2][2]: 30.6
    ● Posición lista_anidada[3]: False
    
    Imprimir la lista resultante por pantalla.
    """
    print("\n=== Ejercicio 10 ===")
    
    # Creamos la lista anidada según las especificaciones
    lista_anidada = [
        15,                       # Posición 0
        True,                     # Posición 1
        [25.5, 57.9, 30.6],       # Posición 2 (que es una lista anidada)
        False                     # Posición 3
    ]
    
    # Imprimimos la lista completa
    print("Lista anidada completa:", lista_anidada)
    
    # Verificamos que cada elemento esté en la posición correcta
    print("\nVerificación de posiciones:")
    print(f"lista_anidada[0]: {lista_anidada[0]}")
    print(f"lista_anidada[1]: {lista_anidada[1]}")
    print(f"lista_anidada[2][0]: {lista_anidada[2][0]}")
    print(f"lista_anidada[2][1]: {lista_anidada[2][1]}")
    print(f"lista_anidada[2][2]: {lista_anidada[2][2]}")
    print(f"lista_anidada[3]: {lista_anidada[3]}")
    
    print("Fin del ejercicio 10")

def menu():
    """
    Muestra un menú para que el usuario seleccione qué ejercicio ejecutar.
    """
    while True:
        print("\n========================================")
        print("PRÁCTICO 5: LISTAS")
        print("========================================")
        print("1. Lista de múltiplos de 4")
        print("2. Lista de 5 elementos y mostrar penúltimo")
        print("3. Lista vacía y agregar elementos con append")
        print("4. Reemplazar elementos en lista de animales")
        print("5. Analizar programa")
        print("6. Lista con saltos de 5 en 5")
        print("7. Reemplazar valores centrales en lista de autos")
        print("8. Lista de dobles")
        print("9. Manipular lista de compras")
        print("10. Crear lista anidada")
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
    print("Bienvenido al Práctico 5 de Listas")
    menu()
