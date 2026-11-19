# Trabajo Práctico Integrador (TPI) — Programación 1

# Tecnicatura Universitaria en Programación — Universidad Tecnológica Nacional (UTN)

# Gestión de Datos de Países en Python

# Descripción del Proyecto

Aplicación de consola desarrollada en **Python 3** para la gestión, consulta y análisis estadístico de información demográfica y geográfica de países. El sistema persiste los registros en un archivo CSV (`paises.csv`) y permite realizar operaciones de alta, actualización, búsqueda, filtrado, ordenamiento y cálculo de métricas globales mediante un menú interactivo en consola.

# Funcionalidades principales

* Listado completo:** Visualización tabular de todos los países cargados desde el dataset.
* Alta de países:** Incorporación de nuevos registros validando campos obligatorios, tipos numéricos y prevención de duplicados (normalizando mayúsculas y tildes).
* Actualización de datos:** Modificación de población y superficie de un país existente con guardado automático en disco.
* Búsqueda por nombre:** Coincidencia exacta o parcial sin distinción de mayúsculas ni acentos.
* Filtrado multi-criterio:** Por continente, por rango de población o por rango de superficie en $\text{km}^2$.
* Ordenamiento configurable:** Por nombre, población o superficie en sentido ascendente o descendente mediante algoritmo de burbuja sobre copia de datos.
* Estadísticas generales:** País con mayor y menor población, promedio de población, promedio de superficie y cantidad de países por continente.

# Estructura del Repositorio

├── integrador.py        # Código fuente principal modularizado
├── paises.csv           # Dataset base en formato CSV (nombre,poblacion,superficie,continente)
├── Informe_TPI.pdf      # Documentación académica y técnica del proyecto
└── README.md            # Documentación general e instrucciones de uso

# Formato del archivo `paises.csv`

El archivo utiliza codificación UTF-8 con encabezado obligatorio `nombre,poblacion,superficie,continente`:

nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa

# Requisitos e Instrucciones de Uso

* Requisitos previos:** Tener instalado **Python 3.x** (no requiere librerías externas; utiliza únicamente el módulo estándar `csv`).
* Clonar o descargar el repositorio:
* Ejecutar el programa: python integrador.py
* (En sistemas Linux/macOS puede requerir `python3 integrador.py`).
   
# Ejemplos de Entradas y Salidas

# 1. Menú Principal y Alta de País (con validación de duplicados)

GESTIÓN DE PAÍSES
1. Listar países
2. Agregar país
3. Actualizar población y superficie
4. Buscar país por nombre
5. Filtrar países
6. Ordenar países
7. Mostrar estadísticas
0. Salir
Elegí una opción: 2
Nombre: Argentina
Continente: América
Población: 45376763
Superficie en km2: 2780400
El país se agregó bien

Elegí una opción: 2
Nombre: argéntina
Continente: América
Ese país ya está cargado

# 2. Búsqueda Parcial y Filtrado por Rango

Elegí una opción: 4
Nombre o parte del nombre: bra

Nombre | Población | Superficie (km2) | Continente
------------------------------------------------------------
Brasil | 213993437 | 8515767 | América

Elegí una opción: 5
1. Continente
2. Rango de población
3. Rango de superficie
Elegí un filtro: 2
Población mínima: 40000000
Población máxima: 150000000

Nombre | Población | Superficie (km2) | Continente
------------------------------------------------------------
Argentina | 45376763 | 2780400 | América
Japón | 125800000 | 377975 | Asia
Alemania | 83149300 | 357022 | Europa

# 3. Ordenamiento y Estadísticas

Elegí una opción: 6
1. Nombre
2. Población
3. Superficie
Ordenar por: 2
¿Descendente? (s/n): s

Nombre | Población | Superficie (km2) | Continente
------------------------------------------------------------
Brasil | 213993437 | 8515767 | América
Japón | 125800000 | 377975 | Asia
Alemania | 83149300 | 357022 | Europa
Argentina | 45376763 | 2780400 | América

Elegí una opción: 7
País con mayor población: Brasil (213993437)
País con menor población: Argentina (45376763)
Promedio de población: 117079875.00
Promedio de superficie: 3007791.00 km2
Cantidad de países por continente:
América: 2
Asia: 1
Europa: 1

# Documentación Académica y Presentación

* Informe Técnico (PDF): Disponible en la raíz de este repositorio bajo el nombre `informe` (incluye marco teórico, diagrama de flujo de operaciones, decisiones técnicas, dificultades y conclusiones).
* Defensa del Proyecto: Presentación oral y demostración en vivo del funcionamiento del sistema en consola.

# Integrantes

* Matias Ramirez
* Gonzalo Larraburú

El proyecto fue diseñado, desarrollado, probado y documentado de manera conjunta y equitativa por ambos integrantes del equipo.
