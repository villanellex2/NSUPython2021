import itertools


class Table:

    def __init__(self, rows, columns, table=None):
        self.rows = rows
        self.columns = columns
        self.table = []
        if table is None:
            for i in range(0, rows):
                self.table.append([0] * columns)
        else:
            for r in table:
                if len(r) < columns:
                    for i in range(len(r), self.columns):
                        r.append(0)
                self.table.append(r.copy())

    def set_row(self, row, values):
        i = 0
        for v in values:
            if i >= self.columns:
                break
            self.table[row][i] = v
            i += 1

    def insert(self, row, column, value):
        self.table[row][column] = value

    def update(self, row, column, new_value):
        self.table[row][column] = new_value

    def remove(self, row, column):
        self.table[row][column] = 0

    def head(self, number):
        res = Table(number, self.columns)
        i = 0
        for row in self.table[:number]:
            res.set_row(i, row)
            i += 1
        return res

    def tail(self, number):
        res = Table(number, self.columns)
        i = 0
        for row in self.table[-number:]:
            res.set_row(i, row)
            i += 1
        return res

    def take_rows(self, rows):
        res = []
        for r in rows:
            res.append(self.table[r])
        return res

    def merge_by_rows(self, t):
        res = Table(self.rows + t.rows, max(self.columns, t.columns))
        i = 0
        for j in self.table:
            res.set_row(i, j)
            i += 1

        for j in t.table:
            res.set_row(i, j)
            i += 1
        return res

    def merge_by_columns(self, t):

        new_table = Table(max(self.rows, t.rows), self.columns + t.columns)
        res = [x + y for x, y in
               itertools.zip_longest(self.table, t.table, fillvalue=[0] * abs(self.columns - t.columns))]
        for r in range(0, len(res)):
            new_table.set_row(r, res[r])
        return new_table

    def take_columns(self, columns):
        res = Table(self.rows, len(columns))
        i = 0
        for r in self.table:
            row = []
            for c in columns:
                row.append(r[c])
            res.set_row(i, row)
            i += 1
        return res

    def to_string(self):
        res = ""
        for j in self.table:
            res += str(j)
            res += "\n"
        return res
