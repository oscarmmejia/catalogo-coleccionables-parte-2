import pytest

from validations import (
    validate_not_empty,
    validate_price,
    validate_status,
    validate_description
)


def test_validate_not_empty_with_valid_value():
    validate_not_empty("Harry Potter", "name")


def test_validate_not_empty_with_empty_string():
    with pytest.raises(ValueError):
        validate_not_empty("", "name")


def test_validate_not_empty_with_spaces():
    with pytest.raises(ValueError):
        validate_not_empty("     ", "name")


def test_validate_price_with_valid_integer():
    validate_price(50)


def test_validate_price_with_valid_float():
    validate_price(45.50)


def test_validate_price_with_negative_number():
    with pytest.raises(ValueError):
        validate_price(-10)


def test_validate_price_with_zero():
    with pytest.raises(ValueError):
        validate_price(0)


def test_validate_price_with_text():
    with pytest.raises(ValueError):
        validate_price("cincuenta")


def test_validate_status_available():
    validate_status("disponible")


def test_validate_status_reserved():
    validate_status("reservada")


def test_validate_status_sold():
    validate_status("vendida")


def test_validate_status_invalid():
    with pytest.raises(ValueError):
        validate_status("agotada")


def test_validate_description_with_used():
    validate_description("Figura usada en buen estado")


def test_validate_description_with_certified():
    validate_description("Figura certificada para coleccionistas")


def test_validate_description_invalid():
    with pytest.raises(ValueError):
        validate_description("Figura en buen estado")