#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
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


def get_gainloss_2_7(stocksFilename, pricesFilename):
    stocks = read_portfolio(stocksFilename)
    prices = dict(read_prices(pricesFilename))

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

    return (total_gain, stocks, prices)


def make_report(stocksFilename, pricesFilename):
    (_, stocks, prices) = get_gainloss_2_7(stocksFilename, pricesFilename)

    print()
    print(" ".join([f"{h:>10s}" for h in ["Name", "Shares", "Price", "Change"]]))
    print(" ".join(["----------" for _ in range(4)]))

    for stock in stocks:
        print(
            f"{stock.name:>10s} "
            + f"{stock.shares:>10d} "
            + f"{usd(stock.price):>10s} "
            + f"{usd(prices[stock.name] - stock.price):>10s}"
        )


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f"Usage: {argv[0]} portfolio prices")

    make_report(argv[1], argv[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
