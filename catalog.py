from validations import validate_not_empty, validate_price, validate_status, validate_description

def add_piece(id, name, category, price, status, description):
    validate_not_empty(id, "id")
    validate_not_empty(name, "name")
    validate_not_empty(category, "category")

    validate_price(price)

    validate_not_empty(status, "status")
    validate_status(status)

    validate_not_empty(description, "description")
    validate_description(description)

    piece = {
        "id": id,
        "name": name,
        "category": category,
        "price": price,
        "status": status,
        "description": description
    }

    return piece

def list_pieces(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    list_pieces_names = []

    for piece in catalog:
        list_pieces_names.append(piece["name"])

    return list_pieces_names

def find_piece_by_id(catalog, id):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    for piece in catalog:
        if piece["id"] == id:
            return piece

    return None

def remove_piece(catalog, id):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    try:
        piece = find_piece_by_id(catalog, id)

        if piece is None:
            raise ValueError("El id introducido no corresponde a ninguna pieza")

        catalog.remove(piece)
        return True

    except ValueError:
        return False

def get_catalog_summary(catalog):
        if not isinstance(catalog, list):
            raise ValueError("El catálogo debe ser una lista")

        summary = {}

        for piece in catalog:
            category = piece["category"]

            if category in summary:
                summary[category] += 1
            else:
                summary[category] = 1

        return summary

def get_pieces_by_category(catalog, category):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    pieces_by_category = []

    for piece in catalog:
        if piece["category"] == category:
            pieces_by_category.append(piece["name"])

    return pieces_by_category

def piece_exists(catalog, id):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    piece = find_piece_by_id(catalog, id)

    if piece is None:
        return False
    return True

def filter_by_status(catalog, status):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    validate_status(status)

    filtered_pieces = []

    for piece in catalog:
        if piece["status"] == status:
            filtered_pieces.append(piece)
    return filtered_pieces

def filter_by_min_price(catalog, min_price):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    if not isinstance(min_price, (int, float)):
        raise ValueError("El precio mínimo debe ser numérico")

    filtered_pieces = []

    for piece in catalog:
        if piece["price"] > min_price:
            filtered_pieces.append(piece)
    return filtered_pieces

def get_average_price(catalog):
    if not isinstance(catalog, list):
        raise ValueError("El catálogo debe ser una lista")

    if len(catalog) == 0:
        return 0

    total_price = 0

    for piece in catalog:
        total_price += piece["price"]

    average_price = total_price / len(catalog)
    return average_price