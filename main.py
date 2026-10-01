from catalog import (
    add_piece,
    list_pieces,
    filter_by_status,
    get_average_price,
    find_piece_by_id,
    remove_piece
)

catalog = []

option = ""

while option != "7":
    print("1. Agregar pieza")
    print("2. Mostrar todas las piezas")
    print("3. Mostrar piezas disponibles")
    print("4. Mostrar precio promedio")
    print("5. Buscar pieza por ID")
    print("6. Eliminar pieza")
    print("7. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        try:
            id = input("Ingrese el identificador: ")
            name = input("Ingrese el nombre: ")
            category = input("Ingrese la categoría: ")
            price = float(input("Ingrese el precio: "))
            status = input("Ingrese el estado")
            description = input("Ingrese la descripción")

            piece = add_piece(id, name, category, price, status, description)
            catalog.append(piece)
            print("Pieza agregada correctamente")
        except ValueError as error:
            print(error)
    elif option == "2":
        pieces = list_pieces(catalog)

        if len(pieces) == 0:
            print("No hay piezas en el catálogo")
        else:
            for name in pieces:
                print(name)