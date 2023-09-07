class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CsvTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HtmlTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """

    def print_row(self, cells, cell_tag):
        print("<tr>", end="")
        for c in cells:
            print(f"<{cell_tag}>{c}</{cell_tag}>", end="")
        print("</tr>")

    def headings(self, headers):
        self.print_row(headers, "th")

    def row(self, rowdata):
        self.print_row(rowdata, "td")
