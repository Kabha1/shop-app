import pytest

from pricing import apply_coupon


def test_welcome10_gives_ten_percent():
    assert apply_coupon(100, "WELCOME10") == 90


def test_vip20_gives_twenty_percent():
    assert apply_coupon(100, "VIP20") == 80


def test_code_works_in_small_letters():
    assert apply_coupon(100, "vip20") == 80


def test_unknown_code_raises_error():
    with pytest.raises(ValueError):
        apply_coupon(100, "FREE20")
