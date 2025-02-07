import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_apple():
    return Product("Apple", "red", 99.9, 1000)


@pytest.fixture
def category_fruit():
    return Category("fruits", "fruits from India", ["banana", "mango"])
