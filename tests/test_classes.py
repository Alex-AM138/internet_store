import pytest

from src.classes import Category, Product


@pytest.fixture
def trial_product():
    """
    Создание тестового товара
    """
    return Product("Iphone 13 Pro", "256GB, Серый цвет", 80000, 13 )


def test_product(trial_product) -> None:
    assert trial_product.name == "Iphone 13 Pro"
    assert trial_product.description == "256GB, Серый цвет"
    assert trial_product.price == 80000
    assert trial_product.quantity == 13


@pytest.fixture
def category_smartphone():
    smartphone_1 = Product("Iphone 13 Pro", "256GB, Серый цвет", 80000, 13 )
    smartphone_2 = Product("Iphone 14 Pro", "512GB, Белый цвет", 120000, 14 )
    return Category('Смартфоны', 'Описание', [smartphone_1, smartphone_2])


@pytest.fixture
def category_tv():
    tv_1 = Product("Samsung", "QLED 8k", 88888, 8)
    tv_2 = Product("LG", "QLED 16k", 161616, 16)
    return Category('Телевизоры', 'Описание', [tv_1,tv_2])


def test_products_and_categories_count(category_smartphone, category_tv):
    assert Category.products_count == 4
    assert Category.categories_count == 2


def test_category(category_smartphone, category_tv):
    assert category_smartphone.name == 'Смартфоны'
    assert category_smartphone.description == 'Описание'
    assert len(category_smartphone.products) == 2
    assert category_smartphone.products[1].name == "Iphone 14 Pro"
    assert category_tv.products[1].description == "QLED 16k"
    assert category_smartphone.products[0].price == 80000
    assert category_tv.products[0].quantity == 8
