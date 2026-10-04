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
            try:
                price = float(input("Ingrese el precio: "))
            except ValueError:
                raise ValueError("El precio debe ser numérico") from None
            status = input("Ingrese el estado")
            description = input("Ingrese la descripción")

            piece = add_piece(id, name, category, price, status, description)
            catalog.append(piece)
            print("Pieza agregada correctamente")
        except ValueError as error:
            print(error)
    elif option == "2":
        try:
            pieces = list_pieces(catalog)

            if len(pieces) == 0:
                print("No hay piezas en el catálogo")
            else:
                for name in pieces:
                    print(name)
        except ValueError as error:
            print(error)

    elif option == "3":
        try:
            available_pieces = filter_by_status(catalog, "disponible")

            if len(available_pieces) == 0:
                print("No hay piezas disponibles")
            else:
                for piece in available_pieces:
                    print(f"{piece['id']} - {piece['name']}")
        except ValueError as error:
            print(error)

    elif option == "4":
        try:
            average_price = get_average_price(catalog)
            print(f"El precio promedio es: {average_price}")
        except ValueError as error:
            print(error)

    elif option == "5":
        try:
            piece_id = input("Ingrese el ID de la pieza a buscar: ")
            piece_searched = find_piece_by_id(catalog, piece_id)

            if piece_searched is None:
                print("El ID introducido no existe")
            else:
                print(piece_searched)
        except ValueError as error:
            print(error)

    elif option == "6":
        try:
            piece_id = input("Ingrese el ID de la pieza a eliminar: ")
            removal_result = remove_piece(catalog, piece_id)

            if removal_result:
                print("Se ha eliminado la pieza")
            else:
                print("No se encontró una pieza con ese ID")
        except ValueError as error:
            print(error)
    elif option == "7":
        print("Gracias por usar el catálogo")
    else:
        print("Ha ingresado una opción invalida")
