from pricing import loyalty_points


def test_points_over_500():
    assert loyalty_points(600) == 60


def test_points_over_100():
    assert loyalty_points(200) == 20


def test_no_points_up_to_100():
    assert loyalty_points(50) == 0
