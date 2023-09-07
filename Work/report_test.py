from os import path

import pytest
from tableformat import (
    TableFormatter,
    TextTableFormatter,
    CsvTableFormatter,
    HtmlTableFormatter,
)
from report import (
    format_report,
    get_gainloss_2_7,
    make_report_data,
    print_report,
    read_portfolio,
    read_prices,
    portfolio_report,
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


def test_print_report(capsys):
    stocks = make_report_data(
        path.join(data_dir, "portfolio.csv"), path.join(data_dir, "prices.csv")
    )
    print_report(stocks)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100      $9.22    -$22.98
       IBM         50    $106.28     $15.18
       CAT        150     $35.46    -$47.98
      MSFT        200     $20.89    -$30.34
        GE         95     $13.48    -$26.89
      MSFT         50     $20.89    -$44.21
       IBM        100    $106.28     $35.84
"""
    )


def test_format_report():
    stocks = make_report_data(
        path.join(data_dir, "portfolio.csv"), path.join(data_dir, "prices.csv")
    )
    formatter = TableFormatter()
    with pytest.raises(NotImplementedError):
        format_report(stocks, formatter)


def test_format_report_text(capsys):
    stocks = make_report_data(
        path.join(data_dir, "portfolio.csv"), path.join(data_dir, "prices.csv")
    )
    formatter = TextTableFormatter()
    format_report(stocks, formatter)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """      Name     Shares      Price     Change 
---------- ---------- ---------- ---------- 
        AA        100      $9.22    -$22.98 
       IBM         50    $106.28     $15.18 
       CAT        150     $35.46    -$47.98 
      MSFT        200     $20.89    -$30.34 
        GE         95     $13.48    -$26.89 
      MSFT         50     $20.89    -$44.21 
       IBM        100    $106.28     $35.84 
"""
    )


def test_format_report_csv(capsys):
    stocks = make_report_data(
        path.join(data_dir, "portfolio.csv"), path.join(data_dir, "prices.csv")
    )
    formatter = CsvTableFormatter()
    format_report(stocks, formatter)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """Name,Shares,Price,Change
AA,100,$9.22,-$22.98
IBM,50,$106.28,$15.18
CAT,150,$35.46,-$47.98
MSFT,200,$20.89,-$30.34
GE,95,$13.48,-$26.89
MSFT,50,$20.89,-$44.21
IBM,100,$106.28,$35.84
"""
    )


def test_format_report_html(capsys):
    stocks = make_report_data(
        path.join(data_dir, "portfolio.csv"), path.join(data_dir, "prices.csv")
    )
    formatter = HtmlTableFormatter()
    format_report(stocks, formatter)
    captured = capsys.readouterr()
    assert (
        captured.out
        == """<tr><th>Name</th><th>Shares</th><th>Price</th><th>Change</th></tr>
<tr><td>AA</td><td>100</td><td>$9.22</td><td>-$22.98</td></tr>
<tr><td>IBM</td><td>50</td><td>$106.28</td><td>$15.18</td></tr>
<tr><td>CAT</td><td>150</td><td>$35.46</td><td>-$47.98</td></tr>
<tr><td>MSFT</td><td>200</td><td>$20.89</td><td>-$30.34</td></tr>
<tr><td>GE</td><td>95</td><td>$13.48</td><td>-$26.89</td></tr>
<tr><td>MSFT</td><td>50</td><td>$20.89</td><td>-$44.21</td></tr>
<tr><td>IBM</td><td>100</td><td>$106.28</td><td>$35.84</td></tr>
"""
    )


def test_portfolio_report_txt(capsys):
    portfolio_report(
        path.join(data_dir, "portfolio.csv"), path.join(data_dir, "prices.csv"), "txt"
    )
    captured = capsys.readouterr()
    assert (
        captured.out
        == """      Name     Shares      Price     Change 
---------- ---------- ---------- ---------- 
        AA        100      $9.22    -$22.98 
       IBM         50    $106.28     $15.18 
       CAT        150     $35.46    -$47.98 
      MSFT        200     $20.89    -$30.34 
        GE         95     $13.48    -$26.89 
      MSFT         50     $20.89    -$44.21 
       IBM        100    $106.28     $35.84 
"""
    )


def test_portfolio_report_unknown():
    with pytest.raises(RuntimeError):
        portfolio_report(
            path.join(data_dir, "portfolio.csv"),
            path.join(data_dir, "prices.csv"),
            "unknown",
        )
