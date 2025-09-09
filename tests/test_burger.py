# tests/test_burger.py
import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


def test_set_buns_assigns_bun():
    """Проверяем, что set_buns корректно устанавливает булочку"""
    burger = Burger()
    bun = Mock()
    bun.get_name.return_value = "Black Bun"
    bun.get_price.return_value = 100.0
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient_appends_to_list():
    """Проверяем, что add_ingredient добавляет ингредиент в конец списка"""
    burger = Burger()
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "Spicy Sauce"
    ingredient.get_price.return_value = 30.0
    burger.add_ingredient(ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient


def test_remove_ingredient_by_index():
    """Проверяем, что remove_ingredient удаляет ингредиент по индексу"""
    burger = Burger()
    ing1 = Mock()
    ing1.get_type.return_value = "SAUCE"
    ing1.get_name.return_value = "Sauce"
    ing1.get_price.return_value = 30
    ing2 = Mock()
    ing2.get_type.return_value = "FILLING"
    ing2.get_name.return_value = "Cutlet"
    ing2.get_price.return_value = 100

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.remove_ingredient(0)

    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ing2


def test_remove_ingredient_invalid_index_raises_error():
    """Проверяем, что при неверном индексе remove_ingredient вызывает IndexError"""
    burger = Burger()
    ingredient = Mock()
    ingredient.get_price.return_value = 100
    burger.add_ingredient(ingredient)

    with pytest.raises(IndexError):
        burger.remove_ingredient(1)


def test_move_ingredient_changes_position():
    """Проверяем, что move_ingredient перемещает ингредиент на новую позицию"""
    burger = Burger()
    ing1 = Mock()
    ing1.get_type.return_value = "SAUCE"
    ing1.get_name.return_value = "Sauce"
    ing1.get_price.return_value = 30
    ing2 = Mock()
    ing2.get_type.return_value = "FILLING"
    ing2.get_name.return_value = "Cutlet"
    ing2.get_price.return_value = 100

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.move_ingredient(0, 1)

    assert burger.ingredients[0] == ing2
    assert burger.ingredients[1] == ing1


@pytest.mark.parametrize("from_idx,to_idx", [
    (2, 0),
], ids=["from-index-out-of-bounds"])
def test_move_ingredient_invalid_index_raises_error(from_idx, to_idx):
    """Проверяем, что move_ingredient вызывает IndexError при выходе за пределы списка"""
    burger = Burger()
    ing1 = Mock()
    ing1.get_price.return_value = 30
    ing2 = Mock()
    ing2.get_price.return_value = 100

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    with pytest.raises(IndexError):
        burger.move_ingredient(from_idx, to_idx)


@pytest.mark.parametrize("bun_price,ingredient_prices,expected,description", [
    (100, [30, 100], 330, "black-bun-with-sauce-and-cutlet"),
    (50, [10], 110, "cheap-bun-with-one-sauce"),
    (80, [], 160, "bun-only-no-ingredients"),
    (75, [20, 20, 20], 210, "medium-bun-with-three-sauces"),
], ids=lambda val: val if isinstance(val, str) else None)
def test_get_price_calculates_total(bun_price, ingredient_prices, expected, description):
    """Проверяем, что get_price корректно считает общую стоимость бургера"""
    burger = Burger()

    bun = Mock()
    bun.get_price.return_value = bun_price
    burger.set_buns(bun)

    for price in ingredient_prices:
        ing = Mock()
        ing.get_price.return_value = price
        burger.add_ingredient(ing)

    assert burger.get_price() == expected


def test_get_receipt_returns_formatted_string():
    """Проверяем, что get_receipt возвращает корректно отформатированный чек"""
    burger = Burger()

    bun = Mock()
    bun.get_name.return_value = "Black Bun"
    bun.get_price.return_value = 100.0

    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "Spicy Sauce"
    sauce.get_price.return_value = 30.0

    cutlet = Mock()
    cutlet.get_type.return_value = "FILLING"
    cutlet.get_name.return_value = "Cutlet"
    cutlet.get_price.return_value = 100.0

    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(cutlet)

    receipt = burger.get_receipt()

    assert "(==== Black Bun ====)" in receipt
    assert "= sauce Spicy Sauce =" in receipt
    assert "= filling Cutlet =" in receipt
    assert "Price: 330.0" in receipt