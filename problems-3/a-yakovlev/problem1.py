from sys import stderr
import copy

class Table():
	"""Simple table realization"""

	def __init__(self, rows=[]):
		self.__rows_num = len(rows)
		self.__columns_num = max(len(row) for row in rows) if len(rows) > 0 else 0
		self.__table=[]
		for row in rows:
			self.add_row(row)


	def __str__(self):
		out = ""
		for row in self.__table:
			out += ' '.join([str(elem) for elem in row]) + '\n'
		return out


	def add_row(self, row):
		if len(row) < self.__columns_num:
			row += [0] * (self.__columns_num - len(row))
		
		elif len(row) > self.__columns_num:
			for row_in in self.__table:
				row_in += [0] * (len(row) - self.__columns_num)
			self.__columns_num = len(row)

		self.__table.append(row)


	def insert(self, row, column, val):
		self.__table[row][column] = val


	def tail(self, num):
		if len(self.__table) < num:
			raise ValueError("Num higher then size of table")
		return Table(copy.deepcopy(self.__table[-num:]))


	def head(self, num):
		if len(self.__table) < num:
			raise ValueError("Num higher then size of table")
		return Table(copy.deepcopy(self.__table[:num]))


	def get_row(self, index):
		return self.__table[i]


	def merge_by_rows(self, table):
		return Table(copy.deepcopy(self.__table) + copy.deepcopy(table.__table))


	def merge_by_columns(self, table):
		new_rows = copy.deepcopy(self.__table)
		new_second_table = copy.deepcopy(table.__table)
		while (len(new_second_table) > len(new_rows)):
			new_rows.append([0] * self.__columns_num)
		for i in range(len(new_second_table)):
			new_rows[i] += new_second_table[i]
		return Table(new_rows)
		


	def get_rows(self, rows_indexes):
		return Table([self.__table[i] for i in rows_indexes])


	def get_columns(self, columns_indexes):
		new_rows = []
		for row in copy.deepcopy(self.__table):
			new_row = []
			for i in columns_indexes:
				new_row.append(row[i])
			new_rows.append(new_row)
		return Table(new_rows)



