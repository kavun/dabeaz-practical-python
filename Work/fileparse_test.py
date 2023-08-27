import pytest
from fileparse import parse_csv


def test_parse_csv_select_3_4():
    assert parse_csv("Data/portfolio.csv", select=["name", "shares"]) == [
        {"name": "AA", "shares": "100"},
        {"name": "IBM", "shares": "50"},
        {"name": "CAT", "shares": "150"},
        {"name": "MSFT", "shares": "200"},
        {"name": "GE", "shares": "95"},
        {"name": "MSFT", "shares": "50"},
        {"name": "IBM", "shares": "100"},
    ]


def test_parse_csv_select_3_5():
    assert parse_csv("Data/portfolio.csv", types=[str, int, float]) == [
        {"price": 32.2, "name": "AA", "shares": 100},
        {"price": 91.1, "name": "IBM", "shares": 50},
        {"price": 83.44, "name": "CAT", "shares": 150},
        {"price": 51.23, "name": "MSFT", "shares": 200},
        {"price": 40.37, "name": "GE", "shares": 95},
        {"price": 65.1, "name": "MSFT", "shares": 50},
        {"price": 70.44, "name": "IBM", "shares": 100},
    ]

    assert parse_csv(
        "Data/portfolio.csv", select=["name", "shares"], types=[str, int]
    ) == [
        {"name": "AA", "shares": 100},
        {"name": "IBM", "shares": 50},
        {"name": "CAT", "shares": 150},
        {"name": "MSFT", "shares": 200},
        {"name": "GE", "shares": 95},
        {"name": "MSFT", "shares": 50},
        {"name": "IBM", "shares": 100},
    ]


def test_parse_csv_no_headers_3_6():
    assert parse_csv("Data/prices.csv", types=[str, float], has_headers=False) == [
        ("AA", 9.22),
        ("AXP", 24.85),
        ("BA", 44.85),
        ("BAC", 11.27),
        ("C", 3.72),
        ("CAT", 35.46),
        ("CVX", 66.67),
        ("DD", 28.47),
        ("DIS", 24.22),
        ("GE", 13.48),
        ("GM", 0.75),
        ("HD", 23.16),
        ("HPQ", 34.35),
        ("IBM", 106.28),
        ("INTC", 15.72),
        ("JNJ", 55.16),
        ("JPM", 36.9),
        ("KFT", 26.11),
        ("KO", 49.16),
        ("MCD", 58.99),
        ("MMM", 57.1),
        ("MRK", 27.58),
        ("MSFT", 20.89),
        ("PFE", 15.19),
        ("PG", 51.94),
        ("T", 24.79),
        ("UTX", 52.61),
        ("VZ", 29.26),
        ("WMT", 49.74),
        ("XOM", 69.35),
    ]


def test_parse_csv_delimiter_3_7():
    assert parse_csv("Data/portfolio.dat", types=[str, int, float], delimiter=" ") == [
        {"name": "AA", "shares": 100, "price": 32.2},
        {"name": "IBM", "shares": 50, "price": 91.1},
        {"name": "CAT", "shares": 150, "price": 83.44},
        {"name": "MSFT", "shares": 200, "price": 51.23},
        {"name": "GE", "shares": 95, "price": 40.37},
        {"name": "MSFT", "shares": 50, "price": 65.1},
        {"name": "IBM", "shares": 100, "price": 70.44},
    ]


def test_parse_csv_exception_3_8():
    with pytest.raises(RuntimeError) as e:
        parse_csv("Data/prices.csv", select=["name", "price"], has_headers=False)
        assert e == "select argument requires column headers"


def test_parse_csv_valueerrors_3_9(capsys):
    portfolio = parse_csv("Data/missing.csv", types=[str, int, float])
    captured = capsys.readouterr()
    assert (
        captured.out
        == """Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
"""
    )
    assert portfolio == [
        {"price": 32.2, "name": "AA", "shares": 100},
        {"price": 91.1, "name": "IBM", "shares": 50},
        {"price": 83.44, "name": "CAT", "shares": 150},
        {"price": 40.37, "name": "GE", "shares": 95},
        {"price": 65.1, "name": "MSFT", "shares": 50},
    ]


def test_parse_csv_silence_errors_3_10():
    portfolio = parse_csv(
        "Data/missing.csv", types=[str, int, float], silence_errors=True
    )
    assert portfolio == [
        {"price": 32.2, "name": "AA", "shares": 100},
        {"price": 91.1, "name": "IBM", "shares": 50},
        {"price": 83.44, "name": "CAT", "shares": 150},
        {"price": 40.37, "name": "GE", "shares": 95},
        {"price": 65.1, "name": "MSFT", "shares": 50},
    ]
