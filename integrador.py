# Trabajo Práctico Integrador - Programación 1

import csv

ARCHIVO_CSV = "paises.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]

def normalizar(texto):
    # Pasa el texto a minúsculas y le saca los espacios y las tildes
    texto = texto.strip().lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    return texto

def cargar_paises():
    # Lee el archivo CSV y devuelve una lista con los países (cada país es un diccionario)
    paises = []
    try:
        archivo = open(ARCHIVO_CSV, "r", encoding="utf-8-sig", newline="")
    except FileNotFoundError:
        print("No se encontró el archivo paises.csv se va a crear al guardar")
        return paises

    lector = csv.DictReader(archivo)
    # Verificamos que el encabezado sea el correcto
    if lector.fieldnames != CAMPOS:
        print("Error el encabezado del archivo CSV no es correcto")
        archivo.close()
        exit()

    numero_fila = 2
    for fila in lector:
        try:
            nombre = fila["nombre"].strip()
            continente = fila["continente"].strip()
            poblacion = int(fila["poblacion"])
            superficie = int(fila["superficie"])
            if nombre == "" or continente == "" or poblacion < 0 or superficie <= 0:
                print(f"Aviso la fila {numero_fila} tiene datos inválidos no se cargó")
            else:
                pais = {"nombre": nombre, "poblacion": poblacion,
                        "superficie": superficie, "continente": continente}
                paises.append(pais)
        except (ValueError, TypeError, AttributeError):
            print(f"Aviso la fila {numero_fila} tiene datos inválidos no se cargó")
        numero_fila += 1

    archivo.close()
    return paises

def guardar_paises(paises):
    # Guarda todos los países en el archivo CSV
    try:
        archivo = open(ARCHIVO_CSV, "w", encoding="utf-8", newline="")
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(paises)
        archivo.close()
        return True
    except OSError:
        print("Error no se pudo guardar el archivo")
        return False

def pedir_entero(mensaje, minimo):
    # Pide un número entero y lo repite hasta que sea válido
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"El número tiene que ser mayor o igual a {minimo}")
            else:
                return valor
        except ValueError:
            print("Error ingresá un número entero")

def mostrar_paises(paises):
    # Muestra una lista de países
    if len(paises) == 0:
        print("No hay países para mostrar")
        return
    print("\nNombre | Población | Superficie (km2) | Continente")
    print("-" * 60)
    for pais in paises:
        print(f"{pais['nombre']} | {pais['poblacion']} | {pais['superficie']} | {pais['continente']}")

def existe_pais(paises, nombre):
    # Devuelve True si el país ya está en la lista
    for pais in paises:
        if normalizar(pais["nombre"]) == normalizar(nombre):
            return True
    return False

def agregar_pais(paises):
    # Agrega un país nuevo
    nombre = input("Nombre: ").strip()
    continente = input("Continente: ").strip()
    if nombre == "" or continente == "":
        print("El nombre y el continente no pueden estar vacíos")
        return
    if existe_pais(paises, nombre):
        print("Ese país ya está cargado")
        return
    poblacion = pedir_entero("Población: ", 0)
    superficie = pedir_entero("Superficie en km2: ", 1)
    pais = {"nombre": nombre, "poblacion": poblacion,
            "superficie": superficie, "continente": continente}
    paises.append(pais)
    if guardar_paises(paises):
        print("El país se agregó bien")

def actualizar_pais(paises):
    # Cambia la población y la superficie de un país
    nombre = normalizar(input("Nombre del país a actualizar: "))
    for pais in paises:
        if normalizar(pais["nombre"]) == nombre:
            pais["poblacion"] = pedir_entero("Nueva población: ", 0)
            pais["superficie"] = pedir_entero("Nueva superficie en km2: ", 1)
            if guardar_paises(paises):
                print("Los datos se actualizaron bien")
            return
    print("No se encontró ese país")

def buscar_pais(paises):
    # Busca países por nombre (sirve el nombre completo o una parte)
    consulta = normalizar(input("Nombre o parte del nombre: "))
    if consulta == "":
        print("No escribiste nada para buscar")
        return
    encontrados = []
    for pais in paises:
        if consulta in normalizar(pais["nombre"]):
            encontrados.append(pais)
    mostrar_paises(encontrados)

def filtrar_paises(paises):
    # Filtra los países por continente o por rango de población o superficie
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")
    opcion = input("Elegí un filtro: ").strip()
    resultado = []

    if opcion == "1":
        continente = normalizar(input("Continente: "))
        for pais in paises:
            if normalizar(pais["continente"]) == continente:
                resultado.append(pais)
    elif opcion == "2":
        minimo = pedir_entero("Población mínima: ", 0)
        maximo = pedir_entero("Población máxima: ", minimo)
        for pais in paises:
            if pais["poblacion"] >= minimo and pais["poblacion"] <= maximo:
                resultado.append(pais)
    elif opcion == "3":
        minimo = pedir_entero("Superficie mínima: ", 1)
        maximo = pedir_entero("Superficie máxima: ", minimo)
        for pais in paises:
            if pais["superficie"] >= minimo and pais["superficie"] <= maximo:
                resultado.append(pais)
    else:
        print("Opción inválida")
        return

    mostrar_paises(resultado)

def ordenar_paises(paises):
    # Ordena los países con el método de burbuja
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    opcion = input("Ordenar por: ").strip()
    if opcion == "1":
        campo = "nombre"
    elif opcion == "2":
        campo = "poblacion"
    elif opcion == "3":
        campo = "superficie"
    else:
        print("Opción inválida")
        return

    descendente = input("¿Descendente? (s/n): ").strip().lower()
    if descendente != "s" and descendente != "n":
        print("Tenés que ingresar s o n")
        return

    # Hacemos una copia para no modificar la lista original
    lista = paises.copy()
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            valor1 = lista[j][campo]
            valor2 = lista[j + 1][campo]
            if campo == "nombre":
                valor1 = normalizar(valor1)
                valor2 = normalizar(valor2)
            # Decidimos si hay que intercambiar los dos países
            if descendente == "n":
                intercambiar = valor1 > valor2
            else:
                intercambiar = valor1 < valor2
            if intercambiar:
                auxiliar = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = auxiliar

    mostrar_paises(lista)

def mostrar_estadisticas(paises):
    # Muestra las estadísticas de los países
    if len(paises) == 0:
        print("No hay datos para calcular estadísticas")
        return

    mayor = paises[0]
    menor = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    por_continente = {}

    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]
        # Contamos los países de cada continente
        continente = pais["continente"]
        if continente in por_continente:
            por_continente[continente] += 1
        else:
            por_continente[continente] = 1

    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de población: {suma_poblacion / len(paises):.2f}")
    print(f"Promedio de superficie: {suma_superficie / len(paises):.2f} km2")
    print("Cantidad de países por continente:")
    for continente in por_continente:
        print(f"{continente}: {por_continente[continente]}")

def mostrar_menu():
    # Muestra el menú principal
    print("\nGESTIÓN DE PAÍSES")
    print("1. Listar países")
    print("2. Agregar país")
    print("3. Actualizar población y superficie")
    print("4. Buscar país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("0. Salir")

def main():
    # Carga los datos y repite el menú hasta que el usuario elija salir
    paises = cargar_paises()
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()
        if opcion == "1":
            mostrar_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            filtrar_paises(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("Sesión finalizada")
        else:
            print("Opción inválida elegí un número del menú")

main()