# Catálogo de Coleccionables - Python Nivel II

## Objetivo

Desarrollar un programa de consola en Python que permita gestionar un catálogo básico de piezas coleccionables.

El proyecto aplica conceptos de Python como funciones, listas, diccionarios, condicionales, bucles, validaciones, manejo de errores, excepciones y organización del código en módulos.

## Contexto

Este proyecto es una evolución del catálogo de coleccionables desarrollado anteriormente.

Cada pieza del catálogo contiene la siguiente información:

- ID
- Nombre
- Categoría
- Precio
- Estado
- Descripción

Los estados permitidos son:

- `disponible`
- `reservada`
- `vendida`

Además, la descripción debe contener obligatoriamente la palabra `usada` o `certificada`.

## Funcionalidades

El programa permite:

- Agregar nuevas piezas al catálogo.
- Validar los datos antes de registrar una pieza.
- Mostrar los nombres de todas las piezas.
- Buscar una pieza por su identificador.
- Eliminar una pieza del catálogo.
- Comprobar si una pieza existe.
- Mostrar piezas pertenecientes a una categoría.
- Mostrar un resumen de piezas por categoría.
- Filtrar piezas por estado.
- Filtrar piezas por precio mínimo.
- Calcular el precio promedio del catálogo.
- Manejar errores utilizando `try`, `except` y `raise`.

## Estructura del proyecto

```text
catalogo-coleccionables/
├── main.py
├── catalog.py
├── validations.py
├── test_catalog.py
├── test_validations.py
└── README.md
```

### `main.py`

Contiene el menú principal y la interacción con el usuario mediante la terminal.

### `catalog.py`

Contiene las funciones relacionadas con la gestión y consulta del catálogo.

### `validations.py`

Contiene las funciones encargadas de validar los datos de las piezas.

### `test_catalog.py`

Contiene pruebas automatizadas de las funciones del catálogo utilizando `pytest`.

### `test_validations.py`

Contiene pruebas automatizadas de las funciones de validación utilizando `pytest`.

## Ejemplo de interacción

```text
1. Agregar pieza
2. Mostrar todas las piezas
3. Mostrar piezas disponibles
4. Mostrar precio promedio
5. Buscar pieza por ID
6. Eliminar pieza
7. Salir

Seleccione una opción: 1

Ingrese el identificador: 001
Ingrese el nombre: Figura Harry Potter
Ingrese la categoría: fantasia
Ingrese el precio: 45.50
Ingrese el estado: disponible
Ingrese la descripción: Figura certificada de Harry Potter en buen estado

Pieza agregada correctamente
```

Ejemplo de validación:

```text
Ingrese el precio: -10

El precio debe ser mayor que cero
```

## Tecnologías y herramientas utilizadas

- Python 3
- Git
- GitHub
- pytest
- PyCharm

## Cómo ejecutar el programa

1. Clonar el repositorio:

```bash
git clone https://github.com/oscarmmejia/catalogo-coleccionables-parte-2.git
```

2. Entrar en la carpeta del proyecto:

```bash
cd catalogo-coleccionables
```

3. Ejecutar el programa:

```bash
python main.py
```

## Ejecutar las pruebas

Instalar `pytest` si no está disponible:

```bash
pip install pytest
```

Ejecutar todas las pruebas:

```bash
pytest -v
```

Las pruebas comprueban, entre otros casos:

- precios válidos e inválidos;
- estados permitidos e incorrectos;
- descripciones válidas e inválidas;
- creación de piezas;
- búsquedas;
- eliminación;
- filtros;
- resumen por categorías;
- cálculo del precio promedio.

## Conceptos aplicados

Durante el desarrollo se utilizaron:

- Variables y tipos de datos.
- Strings.
- Listas.
- Diccionarios.
- Operadores.
- Condicionales.
- Bucles.
- Funciones y parámetros.
- `return`.
- Validaciones.
- `try / except`.
- `raise`.
- Módulos.
- Git y GitHub.
- Pruebas automatizadas con `pytest`.

## Autor

Oscar Mejía

