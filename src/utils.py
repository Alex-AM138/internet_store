import json
import os
from pathlib import Path

from src.classes import Category, Product

ROOT_DIR = Path(__file__).resolve().parent.parent


def json_reader(filename: str = "") -> dict:
    """
    Функция для чтения JSON - файла.
    """
    data = json.load(open(os.path.join(ROOT_DIR, "data", filename)))
    return data


def load_obj_from_json(file) -> list:
    """
    Функция на вход принимает данные из JSON - файла и выводит класс категории товаров.
    """
    categories = []
    for category in file:
        products = []
        for product in category["products"]:
            name_of_product = product["name"]
            description_of_product = product["description"]
            price_of_product = product["price"]
            quantity_of_product = product["quantity"]
            products.append(
                Product(
                    name_of_product,
                    description_of_product,
                    price_of_product,
                    quantity_of_product,
                )
            )
        name_of_category = category["name"]
        description_of_category = category["description"]
        categories.append(Category(name_of_category, description_of_category, products))

    return categories
