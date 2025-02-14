class Product:
    """
    Класс для представления товара.
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс для представления категории товаров.
    """
    name: str
    description: str
    product: list
    categories_count = 0
    products_count = 0



    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.categories_count += 1
        Category.products_count += len(products)