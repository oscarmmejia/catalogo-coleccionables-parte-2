def validate_not_empty(value, field_name):
    if value.strip() == "":
        raise ValueError(f"El campo {field_name} no puede estar vacío")

def validate_price(price):
    if not isinstance(price, (int, float)):
        raise ValueError("El precio debe ser numérico")
    if price <= 0:
        raise ValueError("El precio debe ser mayor que cero")

def validate_status(status):
    if status not in ("disponible", "reservada", "vendida"):
        raise ValueError("El estado debe ser: disponible, reservada o vendida")

def validate_description(description):
    if "usada" not in description.lower() and "certificada" not in description.lower():
        raise ValueError("La descripción debe contener: usada o certificada")