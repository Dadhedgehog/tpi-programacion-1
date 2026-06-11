"""

Materia: Programación 1
Trabajo Práctico Integrador (TPI)
Título: Gestión de Datos de Países 
"""

import csv
import os

ARCH_CSV = "paises.csv"

# 1. PERSISTENCIA Y CARGA DE DATOS (CSV)


def cargar_datos(ruta_archivo):
    """Lee el archivo CSV y retorna una lista de diccionarios con los países."""
    lista_paises = []
    if not os.path.exists(ruta_archivo):
        # Si el archivo no existe, se crea uno vacío con la cabecera
        with open(ruta_archivo, mode='w', encoding='utf-8', newline='') as f:
            escritor = csv.writer(f)
            escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
        return lista_paises

    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    # Validar y transformar tipos de datos requeridos
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    if pais["nombre"] and pais["continente"]:
                        lista_paises.append(pais)
                except (ValueError, KeyError):
                    # Control de errores de formato en filas específicas
                    print(f"Advertencia: Fila mal formateada omitida en CSV.")
    except Exception as e:
        print(f"Error crítico al leer el archivo: {e}")
    return lista_paises


def guardar_datos(ruta_archivo, lista_paises):
    """Guarda la lista de diccionarios actual en el archivo CSV."""
    try:
        with open(ruta_archivo, mode='w', encoding='utf-8', newline='') as f:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            for pais in lista_paises:
                escritor.writerow(pais)
        return True
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
        return False


# 2. VALIDACIONES DE ENTRADA

def leer_entero_positivo(mensaje):
    """Solicita un número entero y valida que sea mayor que cero."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Error: El valor debe ser un número entero mayor a 0.")
        except ValueError:
            print("Error: Entrada inválida. Ingrese un número entero.")


def leer_cadena_no_vacia(mensaje):
    """Solicita una cadena de texto y valida que no esté en blanco."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: Este campo no puede quedar vacío.")


# 3. FUNCIONALIDADES DE GESTIÓN (ABM)

def agregar_pais(lista_paises):
    """Permite añadir un nuevo país validando que no esté duplicado."""
    print("\n--- AGREGAR NUEVO PAÍS ---")
    nombre = leer_cadena_no_vacia("Ingrese el nombre del país: ")
    
    # Validar duplicados (case-insensitive)
    for p in lista_paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"Error: El país '{nombre}' ya se encuentra registrado.")
            return

    poblacion = leer_entero_positivo("Ingrese la población: ")
    superficie = leer_entero_positivo("Ingrese la superficie en km²: ")
    continente = leer_cadena_no_vacia("Ingrese el continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais)
    if guardar_datos(ARCH_CSV, lista_paises):
        print(f"¡Éxito: '{nombre}' ha sido agregado correctamente!")


def actualizar_pais(lista_paises):
    """Modifica la población y superficie de un país existente."""
    print("\n--- ACTUALIZAR DATOS DE PAÍS ---")
    nombre_buscar = leer_cadena_no_vacia("Ingrese el nombre del país a actualizar: ")
    
    for p in lista_paises:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(f"Datos actuales de {p['nombre']}: Población: {p['poblacion']} | Superficie: {p['superficie']} km²")
            nueva_pob = leer_entero_positivo("Ingrese la nueva población: ")
            nueva_sup = leer_entero_positivo("Ingrese la nueva superficie en km²: ")
            
            p["poblacion"] = nueva_pob
            p["superficie"] = nueva_sup
            
            if guardar_datos(ARCH_CSV, lista_paises):
                print(f"¡Éxito: Datos de '{p['nombre']}' actualizados correctamente!")
            return
            
    print(f"Error: No se encontró ningún país con el nombre '{nombre_buscar}'.")


# 4. BÚSQUEDA Y FILTRADOS


def buscar_pais_nombre(lista_paises):
    """Busca países por coincidencia exacta o parcial en el nombre."""
    print("\n--- BUSCAR PAÍS POR NOMBRE ---")
    busqueda = leer_cadena_no_vacia("Ingrese el nombre (o parte de él): ").lower()
    resultados = [p for p in lista_paises if busqueda in p["nombre"].lower()]
    
    mostrar_tabla_paises(resultados)


def filtrar_paises(lista_paises):
    """Submenú para aplicar filtros por continente, población o superficie."""
    print("\n--- FILTRAR PAÍSES ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    opcion = input("Seleccione una opción de filtrado: ")

    if opcion == "1":
        cont = leer_cadena_no_vacia("Ingrese el continente a filtrar: ").lower()
        res = [p for p in lista_paises if p["continente"].lower() == cont]
        mostrar_tabla_paises(res)
    elif opcion == "2":
        min_pob = leer_entero_positivo("Ingrese población mínima: ")
        max_pob = leer_entero_positivo("Ingrese población máxima: ")
        if min_pob > max_pob:
            print("Error: El mínimo no puede ser mayor al máximo.")
            return
        res = [p for p in lista_paises if min_pob <= p["poblacion"] <= max_pob]
        mostrar_tabla_paises(res)
    elif opcion == "3":
        min_sup = leer_entero_positivo("Ingrese superficie mínima (km²): ")
        max_sup = leer_entero_positivo("Ingrese superficie máxima (km²): ")
        if min_sup > max_sup:
            print("Error: El mínimo no puede ser mayor al máximo.")
            return
        res = [p for p in lista_paises if min_sup <= p["superficie"] <= max_sup]
        mostrar_tabla_paises(res)
    else:
        print("Opción de filtrado inválida.")


# 5. ALGORITMOS DE ORDENAMIENTO (MÉTODO BURBUJA)


def ordenar_paises(lista_paises):
    """Ordena los países basándose en un criterio y orden seleccionado por el usuario."""
    print("\n--- ORDENAR PAÍSES ---")
    print("Criterios disponibles: 1. Nombre | 2. Población | 3. Superficie")
    criterio_opc = input("Seleccione el criterio (1-3): ")
    
    if criterio_opc == "1":
        clave = "nombre"
    elif criterio_opc == "2":
        clave = "poblacion"
    elif criterio_opc == "3":
        clave = "superficie"
    else:
        print("Criterio inválido.")
        return

    print("Sentido: 1. Ascendente | 2. Descendente")
    sentido_opc = input("Seleccione el sentido (1-2): ")
    
    if sentido_opc == "1":
        descendente = False
    elif sentido_opc == "2":
        descendente = True
    else:
        print("Sentido inválido.")
        return

    # Clonamos la lista original para no alterar el orden del archivo CSV base
    lista_ordenada = list(lista_paises)
    n = len(lista_ordenada)

    # Implementación manual de Bubble Sort (Ordenamiento Burbuja)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = lista_ordenada[j][clave]
            val2 = lista_ordenada[j+1][clave]
            
            # Si el criterio es el nombre, normalizamos a minúsculas para un orden alfabético correcto
            if clave == "nombre":
                val1 = val1.lower()
                val2 = val2.lower()

            intercambiar = val1 > val2 if not descendente else val1 < val2
            
            if intercambiar:
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]

    mostrar_tabla_paises(lista_ordenada)


# 6. ESTADÍSTICAS BÁSICAS


def mostrar_estadisticas(lista_paises):
    """Calcula y despliega las métricas e indicadores clave del dataset."""
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    if not lista_paises:
        print("No hay datos cargados para generar estadísticas.")
        return

    # Inicializaciones para extremos
    p_mayor_pob = lista_paises[0]
    p_menor_pob = lista_paises[0]
    suma_pob = 0
    suma_sup = 0
    conteo_continentes = {}

    for p in lista_paises:
        # Extremos de Población
        if p["poblacion"] > p_mayor_pob["poblacion"]:
            p_mayor_pob = p
        if p["poblacion"] < p_menor_pob["poblacion"]:
            p_menor_pob = p
        
        # Acumuladores para promedios
        suma_pob += p["poblacion"]
        suma_sup += p["superficie"]
        
        # Frecuencia de continentes (Mapeo)
        cont = p["continente"]
        conteo_continentes[cont] = conteo_continentes.get(cont, 0) + 1

    total_paises = len(lista_paises)
    prom_pob = suma_pob / total_paises
    prom_sup = suma_sup / total_paises

    print(f"-> País con MAYOR población: {p_mayor_pob['nombre']} ({p_mayor_pob['poblacion']} hab.)")
    print(f"-> País con MENOR población: {p_menor_pob['nombre']} ({p_menor_pob['poblacion']} hab.)")
    print(f"-> Promedio de población global: {prom_pob:,.2f} habitantes")
    print(f"-> Promedio de superficie global: {prom_sup:,.2f} km²")
    print("\nCantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"   - {continente}: {cantidad}")

# 7. INTERFAZ AUXILIAR DE SALIDA

def mostrar_tabla_paises(lista):
    """Imprime una lista de países formateada en una tabla limpia de consola."""
    if not lista:
        print("\n[!] No se encontraron resultados que coincidan con la búsqueda o filtro.")
        return

    print("\n" + "="*75)
    print(f"{'Nombre':<20} | {'Población':<15} | {'Superficie (km²)':<18} | {'Continente':<15}")
    print("-"*75)
    for p in lista:
        print(f"{p['nombre']:<20} | {p['poblacion']:<15,} | {p['superficie']:<18,} | {p['continente']:<15}")
    print("="*75)
    print(f"Total de registros mostrados: {len(lista)}\n")


# BUCLE PRINCIPAL (MENÚ DE OPCIONES)


def menu_principal():
    paises = cargar_datos(ARCH_CSV)
    
    while True:
        print("\n" + "='="*12)
        print("  SISTEMA DE GESTIÓN DE PAÍSES UTN")
        print("='="*12)
        print("1. Mostrar todos los países")
        print("2. Agregar un nuevo país")
        print("3. Actualizar datos de un país")
        print("4. Buscar país por nombre")
        print("5. Filtrar países (Continente / Rangos)")
        print("6. Ordenar países (Nombre / Población / Superficie)")
        print("7. Ver Estadísticas Generales")
        print("8. Salir del Sistema")
        
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == "1":
            mostrar_tabla_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais_nombre(paises)
        elif opcion == "5":
            filtrar_paises(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
        elif opcion == "8":
            print("\n¡Gracias por utilizar el sistema! Guardando cambios finales... Saliendo.")
            break
        else:
            print("Opción inválida. Intente nuevamente ingresando un número del 1 al 8.")

if __name__ == "__main__":
    menu_principal()