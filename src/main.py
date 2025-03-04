from src.classes import Category, Product, LawnGrass, Smartphone

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)


grass1 = LawnGrass("Marivanna",
                   "GreenGrass",
                   666,
                   6,
                   "Africa",
                   "6 weeks",
                   "green"
                   )

grass2 = LawnGrass("Marivanna 2.0",
                   "GreenGreenGrass",
                   6666,
                   66,
                   "South Africa",
                   "2 weeks",
                   "light green"
                   )


print(grass1.name)
print(grass1.description)
print(grass1.price)
print(grass1.quantity)
print(grass1.country)
print(grass1.germination_period)
print(grass1.color)

print(grass2.name)
print(grass2.description)
print(grass2.price)
print(grass2.quantity)
print(grass2.country)
print(grass2.germination_period)
print(grass2.color)

phone1 = Smartphone(
        "Смартфон",
        "Современный смартфон",
        30000,
        3,
        "Да",
        "Последняя",
        "123456Gb",
        "green"
                    )

phone2 = Smartphone(
        "Iphone",
        "Popular smartphone",
        80000,
        4,
        "Usual",
        "16",
        "256Gb",
        "grey"
                    )


print(phone1.name)
print(phone1.description)
print(phone1.price)
print(phone1.quantity)
print(phone1.efficiency)
print(phone1.model)
print(phone1.memory)
print(phone1.color)

print(phone2.name)
print(phone2.description)
print(phone2.price)
print(phone2.quantity)
print(phone2.efficiency)
print(phone2.model)
print(phone2.memory)
print(phone2.color)


sum_of_grass = grass1 + grass2
print(sum_of_grass)


sum_of_phones = phone1 + phone2
print(sum_of_phones)


try:
    error1 = grass1 + phone2
except TypeError:
    print("Ошибка TypeError")
else:
    print("No Error")


phone_category = Category(
    "Смартфоны", "Обычные смартфоны", [phone1, phone2]
)
grass_category = Category(
    "Травка", "Совершенно обычная трава", [grass1, grass2]
)

phone_category.add_product(phone2)

print(phone_category.products)

print(Category.product_count)

try:
    phone_category.add_product("Else")
except TypeError:
    print("Ошибка TypeError")
else:
    print("Добавлено")
