def get_row_col(tic_tac):
    tic = tic_tac.upper()
    col = tic[0]
    row = int(tic[1]) - 1
    
    board_keys = {"A": 0, "B": 1, "C": 2}
    for key in board_keys:
        if key == col:
            column = board_keys[key]
            return (row, column)

print(get_row_col("C1"))
print(get_row_col("A3"))
