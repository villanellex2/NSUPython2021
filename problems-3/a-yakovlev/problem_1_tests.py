#!/usr/bin/env python3


from problem1 import Table

t1 = Table([[1,2,3],[2,3,4],[5,6,7,5]])
print("T1 :")
print(t1)

t2 = Table([[3,3,3],[6, 3, 6, 6, 6],[5,6,7,5], [6, 2, 6]])
print("T2 :")
print(t2)

print("Head of t1 is:")
print(t1.head(1))

print("Tail of t1 is:")
print(t1.tail(1))

print("T1 0 and 2 columns:")
print(t1.get_columns([0,2]))

print("T1 0 and 2 rows:")
print(t1.get_rows([0,2]))

print("Merge t1 with t2 by rows")
print(t1.merge_by_rows(t2))

print("Merge t1 with t2 by columns")
print(t1.merge_by_columns(t2))

print(t1)
print("============================================================")
print(t2)