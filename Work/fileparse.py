# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    filename: str,
    select: list = [],
    types: list = [],
    has_headers: bool = True,
    delimiter: str = ",",
    silence_errors: bool = False,
) -> list:
    """
    Parse a CSV file into a list of records
    """
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            orig_headers = next(rows)
            headers = select if select else orig_headers
            indices = [headers.index(name) for name in headers]
        records = []
        for row_num, orig_row in enumerate(rows):
            if not orig_row:
                continue
            row = [orig_row[i] for i in indices] if has_headers else orig_row
            if types:
                row = convert_row(types, row_num + 1, row, silence_errors)
                if row is None:
                    continue
            record = dict(zip(headers, row)) if has_headers else tuple(row)
            records.append(record)
    return records


def convert_row(types: list, row_num: int, row: list, silence_errors: bool) -> list:
    try:
        return [func(field) for func, field in zip(types, row)]
    except ValueError as e:
        if not silence_errors:
            print(f"Row {row_num}: Couldn't convert {row}")
            print(f"Row {row_num}: Reason {e}")
        return None
