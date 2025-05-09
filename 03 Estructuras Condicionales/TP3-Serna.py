# Soluciones TP3 - Estructuras Condicionales en Python

# Ejercicio 1: Verificar si es mayor de edad
def ejercicio1():
    """
    Solicita la edad al usuario y determina si es mayor de edad.
    """
    print("\n--- Ejercicio 1: Verificar si es mayor de edad ---")
    edad = int(input("Ingrese su edad: "))
    
    if edad > 18:
        print("Es mayor de edad")

# Ejercicio 2: Verificar si está aprobado
def ejercicio2():
    """
    Solicita una nota al usuario y determina si está aprobado.
    """
    print("\n--- Ejercicio 2: Verificar si está aprobado ---")
    nota = float(input("Ingrese su nota: "))
    
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

# Ejercicio 3: Verificar si un número es par
def ejercicio3():
    """
    Solicita un número al usuario y verifica si es par.
    """
    print("\n--- Ejercicio 3: Verificar si un número es par ---")
    numero = int(input("Ingrese un número: "))
    
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

# Ejercicio 4: Categoría de edad
def ejercicio4():
    """
    Solicita la edad al usuario y determina a qué categoría pertenece.
    """
    print("\n--- Ejercicio 4: Categoría de edad ---")
    edad = int(input("Ingrese su edad: "))
    
    if edad < 12:
        print("Niño/a")
    elif edad < 18:
        print("Adolescente")
    elif edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

# Ejercicio 5: Verificar longitud de contraseña
def ejercicio5():
    """
    Solicita una contraseña al usuario y verifica su longitud.
    """
    print("\n--- Ejercicio 5: Verificar longitud de contraseña ---")
    contraseña = input("Ingrese una contraseña: ")
    
    if 8 <= len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6: Análisis estadístico
def ejercicio6():
    """
    Analiza una lista de números aleatorios para determinar su sesgo.
    """
    print("\n--- Ejercicio 6: Análisis estadístico ---")
    import random
    from statistics import mode, median, mean
    
    # Generar lista de números aleatorios
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    
    # Calcular parámetros estadísticos
    try:
        moda = mode(numeros_aleatorios)
        mediana = median(numeros_aleatorios)
        media = mean(numeros_aleatorios)
        
        print(f"Lista: {numeros_aleatorios}")
        print(f"Moda: {moda}")
        print(f"Mediana: {mediana}")
        print(f"Media: {media}")
        
        # Determinar el sesgo
        if media > mediana > moda:
            print("Sesgo positivo o a la derecha")
        elif media < mediana < moda:
            print("Sesgo negativo o a la izquierda")
        elif media == mediana == moda:
            print("Sin sesgo")
        else:
            print("No se puede determinar un sesgo claro")
    
    except Exception as e:
        print(f"Error al calcular estadísticas: {e}")
        # Nota: A veces mode() puede fallar si no hay un único valor más frecuente

# Ejercicio 7: Verificar si un string termina con vocal
def ejercicio7():
    """
    Solicita una frase al usuario y verifica si termina con vocal.
    """
    print("\n--- Ejercicio 7: Verificar si un string termina con vocal ---")
    frase = input("Ingrese una frase o palabra: ")
    
    # Verificar si el último carácter es una vocal
    if frase[-1].lower() in "aeiouáéíóú":
        frase += "!"
    
    print(frase)

# Ejercicio 8: Transformar texto según opción
def ejercicio8():
    """
    Transforma un nombre según la opción seleccionada por el usuario.
    """
    print("\n--- Ejercicio 8: Transformar texto según opción ---")
    nombre = input("Ingrese su nombre: ")
    opcion = input("Ingrese una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): ")
    
    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opción no válida. Debe elegir 1, 2 o 3.")

# Ejercicio 9: Clasificar terremotos
def ejercicio9():
    """
    Clasifica un terremoto según la escala de Richter.
    """
    print("\n--- Ejercicio 9: Clasificar terremotos ---")
    magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))
    
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")

# Ejercicio 10: Determinar estación del año
def ejercicio10():
    """
    Determina la estación del año según el hemisferio y la fecha.
    """
    print("\n--- Ejercicio 10: Determinar estación del año ---")
    hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
    mes = int(input("¿Qué mes es? (1-12): "))
    dia = int(input("¿Qué día es? (1-31): "))
    
    # Verificar datos ingresados
    if hemisferio not in ["N", "S"]:
        print("Hemisferio no válido. Debe ser N o S.")
        return
    
    if not (1 <= mes <= 12):
        print("Mes no válido. Debe estar entre 1 y 12.")
        return
    
    if not (1 <= dia <= 31):
        print("Día no válido. Debe estar entre 1 y 31.")
        return
    
    # Determinar período del año
    if (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
        # Desde el 21 de diciembre hasta el 20 de marzo
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        # Desde el 21 de marzo hasta el 20 de junio
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        # Desde el 21 de junio hasta el 20 de septiembre
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:
        # Desde el 21 de septiembre hasta el 20 de diciembre
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    
    # Imprimir resultado según hemisferio
    if hemisferio == "N":
        print(f"En el hemisferio norte, la estación actual es: {estacion_norte}")
    else:
        print(f"En el hemisferio sur, la estación actual es: {estacion_sur}")

# Menú principal para ejecutar los ejercicios
def menu_principal():
    """
    Muestra un menú para seleccionar qué ejercicio ejecutar.
    """
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Verificar si es mayor de edad")
        print("2. Verificar si está aprobado")
        print("3. Verificar si un número es par")
        print("4. Categoría de edad")
        print("5. Verificar longitud de contraseña")
        print("6. Análisis estadístico")
        print("7. Verificar si un string termina con vocal")
        print("8. Transformar texto según opción")
        print("9. Clasificar terremotos")
        print("10. Determinar estación del año")
        print("0. Salir")
        
        opcion = input("\nSeleccione un ejercicio (0-10): ")
        
        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "7":
            ejercicio7()
        elif opcion == "8":
            ejercicio8()
        elif opcion == "9":
            ejercicio9()
        elif opcion == "10":
            ejercicio10()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()
