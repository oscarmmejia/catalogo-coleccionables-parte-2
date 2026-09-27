# Catálogo de Coleccionables

Programa desarrollado en Python para gestionar un catálogo básico
de piezas coleccionables desde la terminal.

El proyecto permite registrar diferentes piezas, almacenar su información, consultar el catálogo y realizar distintas operaciones sobre los datos utilizando los fundamentos de Python.

## Objetivo del programa

El objetivo del proyecto es desarrollar un programa de consola que permita gestionar un pequeño catálogo de piezas coleccionables y, al mismo tiempo, aplicar los principales conceptos de Python estudiados durante el curso.

Cada pieza contiene la siguiente información:

* Identificador.
* Nombre.
* Categoría.
* Precio.
* Estado.
* Descripción.

Las piezas se almacenan mediante **diccionarios de Python**, que posteriormente se incorporan a una **lista** que representa el catálogo completo.

## Contexto del catálogo

El programa simula un catálogo de coleccionables de **Digitech**.

Las piezas pueden pertenecer a diferentes categorías y tener distintos estados, como:

* `disponible`
* `reservada`
* `vendida`

Además del registro de las piezas, el programa permite trabajar con las categorías, consultar información del catálogo y aplicar diferentes filtros.

## Funcionalidades implementadas

El programa incluye las siguientes funcionalidades:

* Registro de 10 piezas coleccionables mediante datos introducidos por terminal.
* Creación de un diccionario para almacenar los datos de cada pieza.
* Almacenamiento de los diccionarios dentro de una lista llamada `catalog`.
* Uso de un conjunto (`set`) para almacenar categorías sin duplicados.
* Visualización del catálogo completo.
* Recorrido de las piezas mediante bucles `for`.
* Visualización individual de los campos de cada pieza.
* Información general del catálogo:

  * Cantidad total de piezas.
  * Cantidad de categorías.
  * Categorías únicas.
* Filtrado de piezas por estado:

  * Disponibles.
  * Reservadas.
  * Vendidas.
* Control de filtros sin resultados.
* Filtrado de piezas a partir de un precio mínimo.
* Uso de operadores lógicos `and`, `or` y `!=`.
* Comprobación de piezas que pueden publicarse.
* Comprobación de piezas que requieren revisión.
* Identificación de piezas que no han sido vendidas.
* Manipulación de strings mediante:

  * Concatenación.
  * Interpolación con f-strings.
  * `split()`.
  * `replace()`.
  * `strip()`.
  * `lower()`.
  * `upper()`.
  * `title()`.
* Introducción y separación de etiquetas mediante comas.
* Normalización de nombres antes de mostrarlos.

## Estructuras de control y manejo de errores

Las partes 10 y 11 del reto eran opcionales y no se desarrollaron específicamente como apartados independientes. La parte 12 se realizó de manera parcial.

Aun así, durante el desarrollo del programa se utilizaron varias de las estructuras relacionadas con estos contenidos.

### Bucles `for`

Los bucles `for` se utilizan para recorrer las piezas almacenadas en `catalog`.

Por ejemplo, permiten revisar cada pieza y acceder individualmente a sus datos:

```python
for pieza in catalog:
    print(f"ID: {pieza['id']} - Nombre: {pieza['name']}")
```

También se utilizan para aplicar filtros sobre todas las piezas sin tener que comprobarlas manualmente una por una.

### Condicionales `if` e `if/else`

Los condicionales permiten tomar decisiones dependiendo de los datos de cada pieza.

Por ejemplo, se utilizan para comprobar si una pieza está disponible:

```python
if pieza["status"] == "disponible":
    print(f"{pieza['name']} está disponible")
```

También se utiliza `if/else` para representar dos posibles resultados:

```python
if pieza["price"] > 0 and pieza["status"] == "disponible":
    print(f"{pieza['name']} - Puede publicarse")
else:
    print(f"{pieza['name']} - No puede publicarse")
```

### Manejo de errores con `try/except`

Aunque la validación completa planteada en la parte 12 no se implementó, el programa sí incorpora manejo básico de errores.

Al solicitar un precio mínimo se utiliza `try/except` para evitar que el programa termine inesperadamente si el usuario introduce un valor que no puede convertirse a número:

```python
try:
    precio_minimo = float(input("Ingrese el precio mínimo: "))
except ValueError:
    print("El precio debe ser un valor numérico")
```

De esta forma, el programa puede detectar una entrada no numérica y mostrar un mensaje comprensible al usuario.

## Ejemplo de interacción

```text
Catalogo de Coleccionables
Bienvenidos al Catalogo de Coleccionables Digitech

Ingrese el identificador de la pieza: 1a
Ingrese el nombre de la pieza: Pikachu
Ingrese la categoria de la pieza: Figuras
Ingrese el precio de la pieza: 30
Ingrese el estado de la pieza: disponible
Ingrese la descripcion de la pieza: Figura usada de Pokemon

{'id': '1a', 'name': 'Pikachu', 'category': 'Figuras', 'price': 30.0, 'status': 'disponible', 'description': 'Figura usada de Pokemon'}
```

Ejemplo de información general:

```text
INFORMACION GENERAL DEL CATALOGO:
Cantidad total de piezas: 10
Cantidad de categorias: 4
Categorias Unicas: {'Figuras', 'Cartas', 'Videojuegos', 'Musica'}
```

Ejemplo de filtro por precio:

```text
Ingrese el precio mínimo: 25
ID: 1a - Nombre: Pikachu - Precio: 30.0
```

## Tecnologías utilizadas

* **Python 3**
* **PyCharm**
* **Git**
* **GitHub**
* Terminal / Git Bash
* Entorno virtual de Python (`.venv`)

## Cómo ejecutar el programa

1. Clonar el repositorio:

```bash
git clone https://github.com/oscarmmejia/catalogo-coleccionables-python.git
```

2. Acceder a la carpeta del proyecto:

```bash
cd catalogo-coleccionables-python
```

3. Ejecutar el archivo principal:

```bash
python main.py
```

También puede ejecutarse directamente desde **PyCharm**, abriendo el proyecto y ejecutando `main.py`.

## Estructura principal del proyecto

```text
catalogo-coleccionables/
├── main.py
├── README.md
└── .gitignore
```

El archivo `main.py` contiene la implementación principal del programa.

## Autor

Proyecto realizado como ejercicio práctico de introducción a Python.

