# Gestión de Datos de Países - UTN TPI

Proyecto integrador desarrollado para la materia **Programación 1** de la Tecnicatura Universitaria en Programación (UTN).

## Descripción del Programa
Este sistema permite gestionar información sobre países (nombre, población, superficie y continente) mediante el uso de estructuras de datos en Python. El programa permite
realizar operaciones de alta, baja, modificación, búsqueda, filtrado, ordenamiento y cálculo de estadísticas, persistiendo los datos en un archivo `.csv`.

## Características Principales
- **ABM:** Agregar nuevos países y actualizar datos poblacionales o de superficie.
- **Búsquedas:** Búsqueda flexible por nombre (parcial o exacta).
- **Filtros:** Capacidad de filtrar registros por continente, rango de población y rango de superficie.
- **Ordenamientos:** Ordenamiento mediante algoritmo *Bubble Sort* por Nombre, Población o Superficie (ascendente o descendente).
- **Estadísticas:** Cálculo automático de promedios y detección de valores extremos.

## Instrucciones de uso
1. Asegúrate de tener instalado **Python 3.x**.
2. Clona este repositorio o descarga los archivos.
3. Asegúrate de que el archivo `paises.csv` esté en la misma carpeta que el script principal.
4. Ejecuta el programa desde la terminal:
   ```bash
   python TPI_Gestion_de_datos_de_paises.py