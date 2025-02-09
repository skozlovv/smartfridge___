import qrcode
import base64

host = "127.0.0.1:5000"


def qrgen(
    name: str,
    category: str,
    date_man: str,
    date_exp: str,
    quantity: float,
    quantity_unit: str,
    nutritional_values: float,
    nutritional_values_unit: str,
    count: float,
    count_unit: str,
):
    """
    name - наименование продукта
    category - категория продукта
    date_man - дата изготовления
    data_exp - дата срока годности
    quantity - количество продукта масса/объем
    quantity_unit - еденицы измерения количество продукта
    nutritional_values - пищевая ценность продукта
    nutritional_values_unit - еденицы измерения пищевой ценности
    count - количество продукта штуки
    count_unit - еденицы измерения количества продукта штук
    """
    product_string = f"{name};{category};{date_man};{date_exp};{quantity};{quantity_unit};{nutritional_values};{nutritional_values_unit};{count};{count_unit}"
    encodded_bytes = base64.urlsafe_b64encode(product_string.encode("utf-8"))
    encoded_string = encodded_bytes.decode("utf-8")
    url = f"http://{host}/qcode/{encoded_string}"
    print(url)
    img = qrcode.make(url)
    img.save("some_file.png")


if __name__ == "__main__":
    qrgen(
        name="Российский",
        category="сыр",
        date_man="02.12.2024",
        date_exp="02.02.2025",
        quantity=200.0,
        quantity_unit="грамм",
        nutritional_values="234.5",
        nutritional_values_unit="ккал",
        count=1.0,
        count_unit="шт",
    )
