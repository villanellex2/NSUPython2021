#!/usr/bin/env python3

import copy


def deep_multiply(obj, n):
    return [copy.deepcopy(obj) for _ in range(n)]


class Table:
    def __init__(self, matrix=None):
        try:
            self._matrix = [*map(list, matrix)] if matrix is not None else None
            self._normalize_lens()
        except (TypeError, ValueError) as e:
            raise ValueError('"matrix" must be of "Iterable[Iterable]" type') from e

    def _normalize_lens(self):
        if self._matrix is None:
            return

        if self._matrix == [[]]:
            self._matrix = [[None]]

        max_len = max(map(len, self._matrix))
        for row in self._matrix:
            row.extend(deep_multiply(None, max_len - len(row)))

    def width(self):
        if self._matrix is None:
            return 0

        return len(self._matrix[0])

    def height(self):
        if self._matrix is None:
            return 0

        return len(self._matrix)

    def head(self, n=3):
        if self._matrix is None:
            return None

        try:
            if n < 1:
                raise ValueError('"n" must be positive')

            return self._matrix[:n]
        except TypeError as e:
            raise ValueError('"n" must be of "int" type') from e

    def tail(self, n=3):
        if self._matrix is None:
            return None

        try:
            if n < 1:
                raise ValueError('"n" must be positive')

            return self._matrix[-n:]
        except TypeError as e:
            raise ValueError('"n" must be of "int" type') from e

    def filtered_rows(self, row_ids):
        try:
            return [self._matrix[row_id] for row_id in row_ids]
        except IndexError as e:
            raise ValueError('"row_ids" contain invalid ids') from e
        except TypeError as e:
            raise ValueError('"row_ids" must be of "Iterable[int]" type') from e

    def filtered_columns(self, column_ids):
        try:
            return [[row[column_id] for row in self._matrix] for column_id in column_ids]
        except IndexError as e:
            raise ValueError('"column_ids" contain invalid ids') from e
        except TypeError as e:
            raise ValueError('"column_ids" must be of "Iterable[int]" type') from e

    def append_row(self, row):
        if self._matrix is None:
            self._matrix = []

        try:
            self._matrix.append(copy.deepcopy(list(row)))
            self._normalize_lens()
        except TypeError as e:
            raise ValueError('"row" must be of "Iterable" type') from e

    def append_column(self, column):
        if self._matrix is None:
            self._matrix = [[]]

        try:
            column_copy = copy.deepcopy(list(column))

            # make matrix and new column the same size
            if len(self._matrix) > len(column_copy):
                column_copy.extend(deep_multiply(None, len(self._matrix) - len(column_copy)))
            elif len(self._matrix) < len(column_copy):
                nones_row = deep_multiply(None, len(self._matrix[0]))
                self._matrix.extend(deep_multiply(nones_row, len(column_copy) - len(self._matrix)))

            for i, row in enumerate(self._matrix):
                row.append(column_copy[i])
        except TypeError as e:
            raise ValueError('"column" must be of "Iterable" type') from e

    def __repr__(self):
        return repr(self._matrix)

    def __str__(self):
        if not self._matrix:
            return 'Table is empty'

        str_matrix = [[str(elem) for elem in row] for row in self._matrix]
        lengths = [max(map(len, column)) for column in zip(*str_matrix)]
        fmt = '\t'.join('{{:{}}}'.format(length) for length in lengths)
        matrix = [fmt.format(*row) for row in str_matrix]
        return '\n'.join(matrix)
