from stock import Stock


def test_stock_4_2():
    s = Stock("GOOG", 100, 490.1)
    assert s.name == "GOOG"
    assert s.shares == 100
    assert s.price == 490.1
    assert s.cost() == 49010.0
    s.sell(25)
    assert s.shares == 75
    assert s.cost() == 36757.5
