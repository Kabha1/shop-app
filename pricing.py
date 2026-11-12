"""Price helpers for Shop App. All prices are in ILS."""

VAT_RATE = 0.18


def apply_discount(price, percent):
    """Return the price after a percent discount."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (100 - percent) / 100, 2)


def add_vat(price, rate=VAT_RATE):
    """Return the price with VAT added."""
    return round(price * (1 + rate), 2)


def cart_total(prices):
    """Return the sum of all prices in the cart."""
    return round(sum(prices), 2)


COUPONS = {"WELCOME10": 10, "VIP20": 20}


def apply_coupon(price, code):
    """Return the price after applying a coupon code."""
    percent = COUPONS.get(code.upper())
    if percent is None:
        raise ValueError("unknown coupon code")
    return apply_discount(price, percent)

FREE_SHIPPING_MIN = 200


def shipping_cost(total):
    """Return the shipping cost in ILS. Free from 200 ILS."""
    if total >= FREE_SHIPPING_MIN:
        return 0
    if total >= 100:
        return 15
    return 30
