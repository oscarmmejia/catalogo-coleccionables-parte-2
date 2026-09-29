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