import pytest

from pricing import add_vat, apply_discount, cart_total


def test_discount_ten_percent():
    assert apply_discount(100, 10) == 90


def test_discount_zero_percent():
    assert apply_discount(50, 0) == 50


def test_discount_rejects_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(100, 150)


def test_add_vat():
    assert add_vat(100) == 118


def test_cart_total():
    assert cart_total([10, 20.5, 5]) == 35.5
