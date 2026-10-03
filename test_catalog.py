import pytest

from catalog import (
    add_piece,
    list_pieces,
    find_piece_by_id,
    remove_piece,
    get_catalog_summary,
    get_pieces_by_category,
    piece_exists,
    filter_by_status,
    filter_by_min_price,
    get_average_price
)


def create_test_catalog():
    return [
        {
            "id": "001",
            "name": "Figura Harry Potter",
            "category": "fantasia",
            "price": 50.0,
            "status": "disponible",
            "description": "Figura certificada de Harry Potter"
        },
        {
            "id": "002",
            "name": "Carta Charizard",
            "category": "anime",
            "price": 100.0,
            "status": "reservada",
            "description": "Carta usada de Charizard"
        },
        {
            "id": "003",
            "name": "Figura Naruto",
            "category": "anime",
            "price": 150.0,
            "status": "vendida",
            "description": "Figura certificada de Naruto"
        }
    ]


# ADD PIECE

def test_add_piece_valid():
    piece = add_piece(
        "004",
        "Lego Fast and Furious",
        "lego",
        40.0,
        "disponible",
        "Pieza Lego usada en buen estado"
    )

    assert piece["id"] == "004"
    assert piece["name"] == "Lego Fast and Furious"
    assert piece["price"] == 40.0


def test_add_piece_negative_price():
    with pytest.raises(ValueError):
        add_piece(
            "004",
            "Lego",
            "lego",
            -10,
            "disponible",
            "Lego usado"
        )


def test_add_piece_invalid_status():
    with pytest.raises(ValueError):
        add_piece(
            "004",
            "Lego",
            "lego",
            40,
            "agotada",
            "Lego usado"
        )


def test_add_piece_invalid_description():
    with pytest.raises(ValueError):
        add_piece(
            "004",
            "Lego",
            "lego",
            40,
            "disponible",
            "Lego en buen estado"
        )


# LIST PIECES

def test_list_pieces():
    catalog = create_test_catalog()

    result = list_pieces(catalog)

    assert result == [
        "Figura Harry Potter",
        "Carta Charizard",
        "Figura Naruto"
    ]


def test_list_pieces_empty_catalog():
    assert list_pieces([]) == []


def test_list_pieces_invalid_catalog():
    with pytest.raises(ValueError):
        list_pieces("esto no es una lista")


# FIND PIECE

def test_find_piece_by_id_existing():
    catalog = create_test_catalog()

    piece = find_piece_by_id(catalog, "002")

    assert piece["name"] == "Carta Charizard"


def test_find_piece_by_id_not_existing():
    catalog = create_test_catalog()

    assert find_piece_by_id(catalog, "999") is None


# REMOVE PIECE

def test_remove_existing_piece():
    catalog = create_test_catalog()

    result = remove_piece(catalog, "001")

    assert result is True
    assert find_piece_by_id(catalog, "001") is None


def test_remove_non_existing_piece():
    catalog = create_test_catalog()

    result = remove_piece(catalog, "999")

    assert result is False


# CATALOG SUMMARY

def test_get_catalog_summary():
    catalog = create_test_catalog()

    result = get_catalog_summary(catalog)

    assert result == {
        "fantasia": 1,
        "anime": 2
    }


# PIECES BY CATEGORY

def test_get_pieces_by_category():
    catalog = create_test_catalog()

    result = get_pieces_by_category(catalog, "anime")

    assert result == [
        "Carta Charizard",
        "Figura Naruto"
    ]


def test_get_pieces_by_category_without_results():
    catalog = create_test_catalog()

    assert get_pieces_by_category(catalog, "musica") == []


# PIECE EXISTS

def test_piece_exists_true():
    catalog = create_test_catalog()

    assert piece_exists(catalog, "001") is True


def test_piece_exists_false():
    catalog = create_test_catalog()

    assert piece_exists(catalog, "999") is False


# FILTER BY STATUS

def test_filter_by_status():
    catalog = create_test_catalog()

    result = filter_by_status(catalog, "disponible")

    assert len(result) == 1
    assert result[0]["name"] == "Figura Harry Potter"


def test_filter_by_invalid_status():
    catalog = create_test_catalog()

    with pytest.raises(ValueError):
        filter_by_status(catalog, "agotada")


# FILTER BY MINIMUM PRICE

def test_filter_by_min_price():
    catalog = create_test_catalog()

    result = filter_by_min_price(catalog, 75)

    assert len(result) == 2
    assert result[0]["price"] > 75
    assert result[1]["price"] > 75


def test_filter_by_min_price_without_results():
    catalog = create_test_catalog()

    assert filter_by_min_price(catalog, 500) == []


def test_filter_by_min_price_with_text():
    catalog = create_test_catalog()

    with pytest.raises(ValueError):
        filter_by_min_price(catalog, "cien")


# AVERAGE PRICE

def test_get_average_price():
    catalog = create_test_catalog()

    result = get_average_price(catalog)

    assert result == 100.0


def test_get_average_price_empty_catalog():
    assert get_average_price([]) == 0