sudoku = [[0 for i in range(9)] for j in range(9)]

with open('output', 'r') as f:
    # skip the head
    [next(f) for x in range(4)]
    solutions = next(f).rstrip('\n')
    sol_array = solutions.split(' ')
    f.close()

try:
    for pos in sol_array:
        i = int(pos[3])-1
        j = int(pos[5])-1
        value = int(pos[7])
        sudoku[i][j] = value
except IndexError:
    print("Unsatisfiable.")
    exit(1)

for row in sudoku:
    print(row)