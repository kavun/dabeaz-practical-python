from os import path
from report import print_report

data_dir = path.join(path.dirname(__file__), "Data")

print_report(path.join(data_dir, "portfolio.csv"), path.join(data_dir, "prices.csv"))
