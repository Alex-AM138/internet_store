import json
from unittest.mock import Mock, patch

import pytest

from src.classes import Category, Product
from src.utils import json_reader, load_obj_from_json


@pytest.fixture
def json_data():
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description":
                "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        },
    ]
    return data


@patch("builtins.open")
def test_json_reader(mock_open, json_data) -> None:
    mock_open.return_value = None
    mock_load = Mock(return_value=json_data)
    json.load = mock_load
    assert json_reader() == json_data


@pytest.fixture
def categories() -> list[Category]:
    category_list = []

    smartphone_1 = Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    smartphone_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    smartphone_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    tv = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category_1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [smartphone_1, smartphone_2, smartphone_3],
    )
    category_2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [tv],
    )

    category_list.append(category_1)
    category_list.append(category_2)
    return category_list


def test_load_obj_from_json(json_data, categories) -> None:
    result = load_obj_from_json(json_data)
    assert result[0].name == categories[0].name
    assert result[0].description == categories[0].description
    assert result[0].products[0].name == categories[0].products[0].name
    assert result[0].products[0].description == categories[0].products[0].description
    assert result[0].products[0].price == categories[0].products[0].price
    assert result[1].name == categories[1].name
    assert result[1].description == categories[1].description
    assert result[1].products[0].name == categories[1].products[0].name
    assert result[1].products[0].description == categories[1].products[0].description
    assert result[1].products[0].price == categories[1].products[0].price
