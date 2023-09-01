from os import path
from report import (
    read_portfolio,
    read_prices,
    get_gainloss_2_7,
)

data_dir = path.join(path.dirname(__file__), "Data")


def test_read_portfolio_2_5():
    portfolio = read_portfolio(path.join(data_dir, "portfolio.csv"))
    assert portfolio[0].name == "AA"
    assert portfolio[0].shares == 100
    assert portfolio[0].price == 32.2


def test_read_prices_2_6():
    prices = dict(read_prices(path.join(data_dir, "prices.csv")))
    assert prices["AA"] == 9.22
    assert prices["AXP"] == 24.85
    assert prices["IBM"] == 106.28
    assert prices["MSFT"] == 20.89


def test_get_gainloss_2_7():
    (gain_loss, _, _) = get_gainloss_2_7(
        path.join(data_dir, "portfolio.csv"), path.join(data_dir, "prices.csv")
    )
    assert round(gain_loss, 2) == -15985.05


def test_report_2_16():
    (gain_loss, _, _) = get_gainloss_2_7(
        path.join(data_dir, "portfoliodate.csv"), path.join(data_dir, "prices.csv")
    )
    assert round(gain_loss, 2) == -15985.05
