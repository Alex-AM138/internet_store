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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        if type(self) is type(other):
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError

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

    def __str__(self):
        total_of_products = 0
        for product in self.__products:
            total_of_products += product.quantity
        return f"{self.name}, количество продуктов: {total_of_products} шт."

    def add_product(self, product):
        if isinstance(product, Product) or issubclass(self.__class__, Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        result = ""
        for products in self.__products:
            result = f"{products.name}, {products.price} руб. Остаток {products.quantity} шт. \n"
        return result


class Iterator:
    """Класс для итерации по категориям"""

    def __init__(self, product_category):
        self.product_category = product_category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if 0 <= self.index < len(self.product_category):
            value = self.product_category[self.index]
            self.index += 1
            return value
        raise StopIteration


class Smartphone(Product):
    """Класс наследователь для смартфонов от класса Product"""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс наследователь для травки от класса Product"""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
