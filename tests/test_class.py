from src.category import Category


def test_init_product(product_apple):
    assert product_apple.name == "Apple"
    assert product_apple.description == "red"
    assert product_apple.price == 99.9
    assert product_apple.quantity == 1000


def test_init_category(category_fruit):
    assert category_fruit.name == "fruits"
    assert category_fruit.description == "fruits from India"
    assert category_fruit.products == ["banana", "mango"]
    assert category_fruit.product_count == 2
    assert Category.category_count == 1
