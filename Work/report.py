#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import csv
from currency import usd
from fileparse import parse_csv, parse_lines


def read_portfolio_2_4(filename):
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        next(rows)  # skip header
        for fields in rows:
            try:
                holding = (fields[0], int(fields[1]), float(fields[2]))
                portfolio.append(holding)
            except ValueError:
                print(f"Could not parse {fields}")
    return portfolio


def read_portfolio(filename):
    with open(filename) as f:
        return parse_lines(
            f, select=["name", "shares", "price"], types=[str, int, float]
        )


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
        market_price = prices[stock["name"]]
        stock["change"] = market_price - stock["price"]
        stock["current_value"] = stock["price"] * stock["shares"]
        stock["market_value"] = market_price * stock["shares"]
        stock["value_gain"] = stock["market_value"] - stock["current_value"]

        total_value += stock["current_value"]
        total_market_value += stock["market_value"]
        total_gain += stock["value_gain"]

    return (total_gain, stocks)


def make_report(stocksFilename, pricesFilename):
    (_, stocks) = get_gainloss_2_7(stocksFilename, pricesFilename)

    print()
    print(" ".join([f"{h:>10s}" for h in ["Name", "Shares", "Price", "Change"]]))
    print(" ".join(["----------" for _ in range(4)]))

    for stock in stocks:
        (name, shares, price, change, _, _, _) = stock.values()
        print(f"{name:>10s} {shares:>10d} {usd(price):>10s} {usd(change):>10s}")


def main(argv):
    if len(argv) != 3:
        raise SystemExit(f"Usage: {argv[0]} portfolio prices")

    make_report(argv[1], argv[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
