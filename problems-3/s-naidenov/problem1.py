from table import Table

if __name__ == '__main__':
    t1 = Table(4, 4)
    print("t1 = \n" + t1.to_string())

    t1.set_row(0, [6, 6, 6, 7])
    t1.set_row(1, [8, 8, 8, 9])
    t1.set_row(3, [9, 9, 9, 9])
    print("t1 = \n" + t1.to_string())

    t2_data = [[1, 2, 3], [4, 5, 6], [7, 8], [10, 11, 12], [13, 15]]
    t2 = Table(5, 3, t2_data)
    print("t2 = \n" + t2.to_string())

    print("t1 head = \n" + t1.head(2).to_string())
    print("t2 tail = \n" + t2.tail(2).to_string())

    print("t1 rows = \n" + str(t1.take_rows([0, 2, 3])))

    print("t2 = \n" + t2.to_string())
    print("t1 = \n" + t1.to_string())
    print("merge t2 and t1 by rows = \n"+t2.merge_by_rows(t1).to_string())

    t2 = Table(4, 4)
    print("t1 = \n" + t1.to_string())

    t2.set_row(0, [6, 6, 6, 7])
    t2.set_row(1, [8, 8, 8, 9])
    t2.set_row(3, [9, 9, 9, 9])

    print("merge t1 and t2 by columns = \n"+t1.merge_by_columns(t2).to_string())
    print("merge t2 and t1 by rows = \n" + t2.merge_by_rows(t1).to_string())

    print("columns from t1 = \n" + t1.take_columns([0,3,2]).to_string())
    t2_data = [[1, 2, 3], [4, 5, 6], [7, 8], [10, 11, 12], [13, 15]]
    t2 = Table(5, 3, t2_data)
    print("columns from t2 = \n" + t2.take_columns([0,2,2]).to_string())