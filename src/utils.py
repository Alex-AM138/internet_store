import json

from src.classes import Product, Category


def json_reader(filename: str) -> dict:
    """
    Функция для чтения JSON - файла.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def load_obj_from_json(file) -> list:
    """
    Функция на вход принимает данные из JSON - файла и выводит класс категории товаров
    """
    categories = []
    for category in file:
        products = []
        for product in category['products']:
            name_of_product = product['name']
            description_of_product = product['description']
            price_of_product = product['price']
            quantity_of_product = product['quantity']
            products.append(Product(name_of_product, description_of_product, price_of_product, quantity_of_product))
        name_of_category = category['name']
        description_of_category = category['description']
        categories.append(Category(name_of_category, description_of_category, products))

    return categories
