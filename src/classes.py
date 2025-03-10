from abc import ABC, abstractmethod


class ZeroQuantityException(Exception):
    """
    Класс, исключение для случая, когда количество товара равно нулю.
    """

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        super().__init__(message)


class MixinLog:
    """
    Класс-миксин, который при создании объекта, то есть при работе метода
    __init__, печатает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект.
    """

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        attributes = []
        for attr, value in self.__dict__.items():
            attributes.append(f"{attr}={value}")
        return f"{self.__class__.__name__}({', '.join(attributes)})"


class BaseProduct(ABC):
    """
    Абстрактный родительский класс для класса Product
    """

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def new_product(self, product_data, product_list=None):
        pass

    @abstractmethod
    def price(self):
        pass


class BaseCategory(ABC):
    """
    Абстрактный родительский класс для класса Category
    """

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def products(self):
        pass


class Product(BaseProduct, MixinLog):
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
        super().__init__()

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


class Category(BaseCategory):
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
            try:
                if product.quantity <= 0:
                    raise ZeroQuantityException
            except ZeroQuantityException as e:
                print(e)
            else:
                self.__products.append(product)
                self.product_count += 1
            finally:
                print("Операция добавления продукта завершена")
        else:
            raise TypeError

    @property
    def products(self):
        result = ""
        for products in self.__products:
            result = f"{products.name}, {products.price} руб. Остаток {products.quantity} шт. \n"
        return result

    def avg_price(self):
        """
        Вычисляет средний ценник всех товаров в категории,
        если товаров нет, то возвращает 0.
        """
        total_amount = 0
        products_quantity = 0

        for product in self.__products:
            total_amount += product.price * product.quantity
            products_quantity += product.quantity

        try:
            avg_price = total_amount / products_quantity
        except ZeroDivisionError:
            return 0
        return round(avg_price, 2)


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


class Order(BaseCategory, MixinLog):
    """
    Класс, который выводит, какой товар был куплен,
    количество купленного товара, а также итоговую стоимость.
    В заказе может быть указан только один товар.
    """

    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("В заказ можно добавить только объект класса Product.")
        if quantity <= 0:
            raise ValueError("Количество товара должно быть больше нуля.")

        self.product = product
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        total_cost = self.product.price * self.quantity
        return (
            f"Заказ: {self.product.name}, {self.quantity} шт.\n"
            f"Цена за единицу: {self.product.price} руб.\n"
            f"Итоговая стоимость: {total_cost} руб."
        )

    def add_product(self, product):
        raise NotImplementedError("В заказе может быть только один товар.")

    @property
    def products(self):
        return f"{self.product.name}, {self.quantity} шт., {self.product.price} руб."
