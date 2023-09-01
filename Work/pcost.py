# pcost.py
#
# Exercise 1.27
from report import read_portfolio


def pcost(filename):
    """Returns the total cost of the portfolio"""
    portfolio = read_portfolio(filename)
    return sum(map(lambda p: p.cost(), portfolio))


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f"Usage: {argv[0]} portfolio")

    cost = pcost(argv[1])
    print(f"Total cost: {cost}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
