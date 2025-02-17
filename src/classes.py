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
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data, product_list=None):
        """
        Создаёт новый объект "Product" или обновляет уже существующий
        """
        if product_list is None:
            product_list = []

        for product in product_list:
            if product.name == product_data["name"]:
                product.quantity += product_data["quantity"]
                if product_data["price"] > product.price:
                    product.price = product_data["price"]
                return product

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена должна быть больше нуля")
        elif new_price < self.__price:
            confirmation = input("Цена снизится. Снизить цену? y/n: ")
            if confirmation.lower() == "y":
                self.__price = new_price
            else:
                print("Изменения отменены")
        else:
            self.__price = new_price


class Category:
    """
    Класс для представления категории товаров.
    """

    name: str
    description: str
    product: list
    categories_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.categories_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            raise Exception

    @property
    def products(self):
        result = ""
        for products in self.__products:
            result = f"{products.name}, {products.price} руб. Остаток {products.quantity} шт. \n"
        return result
