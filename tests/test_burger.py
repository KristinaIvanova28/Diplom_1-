import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data.test_data import (
    get_black_bun,
    get_spicy_sauce,
    get_cutlet,
    BURGER_COMBINATIONS
)


class TestBurger:
    
    def test_set_buns_assigns_bun(self):
        """Проверяем, что set_buns корректно устанавливает булочку"""
        burger = Burger()
        bun = get_black_bun()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_appends_to_list(self):
        """Проверяем, что add_ingredient добавляет ингредиент в конец списка"""
        burger = Burger()
        ingredient = get_spicy_sauce()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient_by_index(self):
        """Проверяем, что remove_ingredient удаляет ингредиент по индексу"""
        burger = Burger()
        sauce = get_spicy_sauce()
        cutlet = get_cutlet()

        burger.add_ingredient(sauce)
        burger.add_ingredient(cutlet)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == cutlet

    def test_remove_ingredient_invalid_index_raises_error(self):
        """Проверяем, что при неверном индексе remove_ingredient вызывает IndexError"""
        burger = Burger()
        cutlet = get_cutlet()
        burger.add_ingredient(cutlet)

        with pytest.raises(IndexError):
            burger.remove_ingredient(1)

    def test_move_ingredient_changes_position(self):
        """Проверяем, что move_ingredient перемещает ингредиент на новую позицию"""
        burger = Burger()
        sauce = get_spicy_sauce()
        cutlet = get_cutlet()

        burger.add_ingredient(sauce)
        burger.add_ingredient(cutlet)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == cutlet
        assert burger.ingredients[1] == sauce

    @pytest.mark.parametrize("from_idx,to_idx", [
        (2, 0),
    ], ids=["from-index-out-of-bounds"])
    def test_move_ingredient_invalid_index_raises_error(self, from_idx, to_idx):
        """Проверяем, что move_ingredient вызывает IndexError при выходе за пределы списка"""
        burger = Burger()
        sauce = get_spicy_sauce()
        cutlet = get_cutlet()

        burger.add_ingredient(sauce)
        burger.add_ingredient(cutlet)

        with pytest.raises(IndexError):
            burger.move_ingredient(from_idx, to_idx)

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected,description", BURGER_COMBINATIONS)
    def test_get_price_calculates_total(self, bun_price, ingredient_prices, expected, description):
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

    def test_get_receipt_returns_formatted_string(self):
        """Проверяем, что get_receipt возвращает корректно отформатированный чек"""
    burger = Burger()

    bun = get_black_bun()
    sauce = get_spicy_sauce()
    cutlet = get_cutlet()

    burger.set_buns(bun)
    burger.add_ingredient(sauce)
    burger.add_ingredient(cutlet)

    receipt = burger.get_receipt()
        
    # Ожидаемый чек с точным форматированием
    expected_receipt = """(==== Black Bun ====)
= sauce Spicy Sauce =
= filling Cutlet =
(==== Black Bun ====)

Price: 330.0"""
        