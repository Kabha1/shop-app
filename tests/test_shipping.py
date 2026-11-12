from pricing import shipping_cost


def test_free_shipping_from_200():
    assert shipping_cost(200) == 0


def test_shipping_15_above_100():
    assert shipping_cost(150) == 15


def test_shipping_30_under_100():
    assert shipping_cost(50) == 30
