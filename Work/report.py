#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
from tableformat import (
    TableFormatter,
    CsvTableFormatter,
    HtmlTableFormatter,
    TextTableFormatter,
)
from currency import usd
from fileparse import parse_lines
from stock import Stock


def read_portfolio(filename):
    with open(filename) as f:
        return [
            Stock(n["name"], n["shares"], n["price"])
            for n in parse_lines(
                f, select=["name", "shares", "price"], types=[str, int, float]
            )
        ]


def read_prices(filename):
    with open(filename) as f:
        return parse_lines(f, types=[str, float], has_headers=False)


def get_gainloss_2_7(stocks_filename, prices_filename):
    stocks = read_portfolio(stocks_filename)
    prices = dict(read_prices(prices_filename))

    total_value = 0.0
    total_market_value = 0.0
    total_gain = 0.0

    for stock in stocks:
        market_price = prices[stock.name]
        market_value = market_price * stock.shares
        value_gain = market_value - stock.cost()
        total_value += stock.cost()
        total_market_value += market_value
        total_gain += value_gain
        stock.change = market_price - stock.price
        stock.market_price = market_price

    return (total_gain, stocks, prices)


def make_report_data(stocks_filename, prices_filename):
    (_, stocks, _) = get_gainloss_2_7(stocks_filename, prices_filename)
    return stocks


def print_report(stocks):
    print()
    print(" ".join([f"{h:>10s}" for h in ["Name", "Shares", "Price", "Change"]]))
    print(" ".join(["----------" for _ in range(4)]))

    for stock in stocks:
        print(
            f"{stock.name:>10s} "
            + f"{stock.shares:>10d} "
            + f"{usd(stock.market_price):>10s} "
            + f"{usd(stock.change):>10s}"
        )


def format_report(stocks, formatter: TableFormatter):
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for stock in stocks:
        formatter.row(
            [stock.name, str(stock.shares), usd(stock.market_price), usd(stock.change)]
        )


def portfolio_report(stocks_filename, prices_filename, format):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    report = make_report_data(stocks_filename, prices_filename)

    # Print it out
    if format == "txt":
        formatter = TextTableFormatter()
    elif format == "csv":
        formatter = CsvTableFormatter()
    elif format == "html":
        formatter = HtmlTableFormatter()
    else:
        raise RuntimeError(f"Unknown format {format}")
    format_report(report, formatter)


def main(argv):
    if len(argv) != 4:
        raise SystemExit(f"Usage: {argv[0]} portfolio prices format")

    portfolio_report(argv[1], argv[2], argv[3])


if __name__ == "__main__":
    import sys

    main(sys.argv)
