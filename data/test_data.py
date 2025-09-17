from unittest.mock import Mock


# Тестовые булки
def get_black_bun():
    bun = Mock()
    bun.get_name.return_value = "Black Bun"
    bun.get_price.return_value = 100.0
    return bun


def get_white_bun():
    bun = Mock()
    bun.get_name.return_value = "White Bun"
    bun.get_price.return_value = 50.0
    return bun


def get_red_bun():
    bun = Mock()
    bun.get_name.return_value = "Red Bun"
    bun.get_price.return_value = 75.0
    return bun


# Тестовые соусы
def get_spicy_sauce():
    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "Spicy Sauce"
    sauce.get_price.return_value = 30.0
    return sauce


def get_sour_cream():
    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "Sour Cream"
    sauce.get_price.return_value = 20.0
    return sauce


# Тестовые начинки
def get_cutlet():
    filling = Mock()
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "Cutlet"
    filling.get_price.return_value = 100.0
    return filling


def get_cheese():
    filling = Mock()
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "Cheese"
    filling.get_price.return_value = 50.0
    return filling


def get_salad():
    filling = Mock()
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "Salad"
    filling.get_price.return_value = 25.0
    return filling


# Комбинации для параметризованных тестов
BURGER_COMBINATIONS = [
    (100, [30, 100], 330, "black-bun-with-sauce-and-cutlet"),
    (50, [10], 110, "cheap-bun-with-one-sauce"),
    (80, [], 160, "bun-only-no-ingredients"),
    (75, [20, 20, 20], 210, "medium-bun-with-three-sauces"),
]