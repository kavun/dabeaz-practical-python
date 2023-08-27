# pcost.py
#
# Exercise 1.27
from report import read_portfolio_2_5


def pcost(filename):
    """Returns the total cost of the portfolio"""
    portfolio = read_portfolio_2_5(filename)
    return sum(map(lambda p: p["shares"] * p["price"], portfolio))
