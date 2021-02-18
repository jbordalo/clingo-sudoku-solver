from problem import problem

with open("sudoku-problem.lp", 'w') as f:
    for i in range(9):
        for j in range(9):
            if problem[i][j] != 0:
                f.write(f"in({i+1},{j+1},{problem[i][j]}).\n")
    f.close()
