import pytest

from src.classes import Category, Iterator, LawnGrass, Order, Product, Smartphone


def test_new_product_creation():
    """
    Проверяем создание нового товара.
    """
    product_data = {
        "name": "Iphone22",
        "description": "Новее нового лучше лучшего",
        "price": 666666,
        "quantity": 10,
    }
    product = Product.new_product(product_data)
    assert product.name == "Iphone22"
    assert product.price == 666666
    assert product.quantity == 10


def test_new_product_update():
    """
    Проверяем обновление существующего товара.
    """
    existing_product = Product("Iphone22", "Новее нового лучше лучшего", 666666, 10)
    product_data = {
        "name": "Iphone22",
        "description": "Новее нового лучше лучшего",
        "price": 7777777,
        "quantity": 5,
    }
    updated_product = Product.new_product(product_data, [existing_product])
    assert updated_product.quantity == 15  # 10 + 5
    assert updated_product.price == 7777777  # Новая цена выше


def test_price_getter():
    """
    Проверяем, что геттер возвращает корректное значение цены.
    """
    product = Product("Iphone22", "Новее нового лучше лучшего", 666666, 10)
    assert product.price == 666666


def test_price_setter_positive():
    """
    Проверяем, что сеттер корректно устанавливает новую цену.
    """
    product = Product("Iphone22", "Новее нового лучше лучшего", 666666, 10)
    product.price = 7777777
    assert product.price == 7777777


def test_price_setter_negative():
    """
    Проверяем, что сеттер не устанавливает цену, если она меньше или равна нулю.
    """
    product = Product("Iphone22", "Новее нового лучше лучшего", 666666, 10)
    product.price = -100
    assert product.price == 666666


def test_price_setter_confirmation(monkeypatch):
    """
    Проверяем, что сеттер запрашивает подтверждение при снижении цены.
    """
    product = Product("Iphone22", "Новее нового лучше лучшего", 666666, 10)

    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 4444
    assert product.price == 4444

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 333
    assert product.price == 4444


def test_category_initialization():
    """
    Проверяем инициализацию категории.
    """
    product1 = Product("Iphone22", "Новее нового лучше лучшего", 666666, 10)
    product2 = Product("Nokia777", "Кирпичик", 30, 20)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [product1, product2],
    )

    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(category._Category__products) == 2
    assert Category.categories_count == 1
    assert Category.product_count == 2


def test_add_product():
    """
    Проверяем добавление товара в категорию.
    """
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [],
    )

    product = Product("Iphone22", "Новее нового лучше лучшего", 666666, 10)

    category.add_product(product)

    assert len(category._Category__products) == 1
    assert Category.product_count == 2

    with pytest.raises(Exception):
        category.add_product("Не товар")


def test_products_getter():
    """
    Проверяем геттер для списка товаров.
    """
    product1 = Product("Iphone22", "Новее нового лучше лучшего", 666666, 10)
    product2 = Product("Nokia777", "Кирпичик", 30, 20)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [product1, product2],
    )

    expected_output = "Nokia777, 30 руб. Остаток 20 шт. \n"
    assert category.products == expected_output


def test_iteration():
    products = ["Ноутбук", "Смартфон", "Планшет"]
    iterator = Iterator(products)

    assert next(iterator) == "Ноутбук"
    assert next(iterator) == "Смартфон"
    assert next(iterator) == "Планшет"

    with pytest.raises(StopIteration):
        next(iterator)


def test_empty_iteration():
    empty_iterator = Iterator([])

    with pytest.raises(StopIteration):
        next(empty_iterator)


def test_reiteration():
    products = ["Ноутбук", "Смартфон"]
    iterator = Iterator(products)

    assert next(iterator) == "Ноутбук"
    assert next(iterator) == "Смартфон"

    iterator.index = 0
    assert next(iterator) == "Ноутбук"
    assert next(iterator) == "Смартфон"


def test_category_init():

    product1 = Product("Ноутбук", "Ноутбук для работы", 50000, 10)
    product2 = Product("Смартфон", "Смартфон обычный", 30000, 5)

    category = Category("Электроника", "Техника для дома и офиса", [product1, product2])

    assert category.name == "Электроника"
    assert category.description == "Техника для дома и офиса"
    assert len(category._Category__products) == 2
    assert Category.categories_count == 4
    assert Category.product_count == 6


def test_category_str():
    product1 = Product("Ноутбук", "Ноутбук для работы", 50000, 10)
    product2 = Product("Смартфон", "Смартфон обычный", 30000, 5)

    category = Category("Электроника", "Техника для дома и офиса", [product1, product2])

    assert str(category) == "Электроника, количество продуктов: 15 шт."


def test_empty_category():
    category = Category("Пустая категория", "Нет продуктов", [])

    assert category.name == "Пустая категория"
    assert category.description == "Нет продуктов"
    assert len(category._Category__products) == 0
    assert str(category) == "Пустая категория, количество продуктов: 0 шт."


def test_product_str():
    product = Product("Смартфон", "Современный смартфон", 30000, 5)

    expected_str = "Смартфон, 30000 руб. Остаток: 5 шт.\n"
    assert str(product) == expected_str


def test_product_addition():
    product1 = Product("Ноутбук", "Мощный ноутбук", 50000, 2)
    product2 = Product("Смартфон", "Современный смартфон", 30000, 3)

    total_cost = product1 + product2
    assert total_cost == 50000 * 2 + 30000 * 3  # 100000 + 90000 = 190000


def test_smartphone_class():
    phone = Smartphone(
        "Смартфон",
        "Современный смартфон",
        30000,
        3,
        "Да",
        "Последняя",
        "123456Gb",
        "green",
    )
    assert phone.name == "Смартфон"
    assert phone.model == "Последняя"
    assert phone.color == "green"
    assert issubclass(phone.__class__, Product)


def test_lawngrass_class():
    grass = LawnGrass("Marivanna", "GreenGrass", 666, 6, "Africa", "6 weeks", "green")
    assert grass.name == "Marivanna"
    assert grass.description == "GreenGrass"
    assert grass.price == 666
    assert grass.quantity == 6
    assert grass.color == "green"
    assert issubclass(grass.__class__, Product)


@pytest.fixture
def smartphones() -> Category:
    phone_1 = Product("Смартфон", "Современный смартфон", 30000, 3)
    phone_2 = Product("Смартфон2", "Смартфон современнее", 40000, 2)
    return Category("Смартфоны", "Описание", [phone_1, phone_2])


@pytest.fixture
def tv() -> Category:
    tv_1 = Product("Телевизор", "большой телевизор", 50000, 2)
    tv_2 = Product("Телевизор", "маленький телевизор", 20000, 2)
    return Category("Телевизоры", "Описание", [tv_1, tv_2])


def test_add_product_multiple_products():
    category = Category("Electronics", "Gadgets and devices", [])

    product1 = Product("Смартфон", "Современный смартфон", 30000, 3)
    product2 = Product("Телевизор", "большой телевизор", 50000, 2)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category._Category__products) == 2
    assert category.product_count == 10


def test_print_mixin(capsys):
    LawnGrass("Marivanna", "GreenGrass", 666, 6, "Africa", "6 weeks", "green")
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "LawnGrass(name=Marivanna, description=GreenGrass, _Product__price=666, quantity=6)"
    )


@pytest.fixture
def sample_product():
    return Product(name="ноутбук", description="для работы", price=1000.0, quantity=2)


def test_order_creation(sample_product):
    order = Order(product=sample_product, quantity=2)
    assert order.product == sample_product
    assert order.quantity == 2
