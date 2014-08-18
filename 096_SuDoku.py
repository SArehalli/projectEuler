text = open('096_sudoku.txt')
grid = []
i = -1 
j = 0
for line in text:
    if line[0] != 'G' and line != '\n':
        grid[i].append([])
        for digit in line[:-1]:
            grid[i][j].append(int(digit))
        j += 1
    elif line != '\n':
        grid.append([])
        i += 1
        j = 0

def solved(puzzle):
    for row in puzzle:
        for number in row:
            if number == 0:
                return False
    return True

def solve(puzzle):                                                      # Simple Sudoku
    while not solved(puzzle):                                           # Is Solved in a Simple Way
        for coord in [(i,j) for i in range(9) for j in range(9)]:       # Guessing is Harder
            if puzzle[coord[0]][coord[1]] == 0:
                sols = list(range(1,10))
                for number in puzzle[coord[0]]:
                    if number in sols:
                        sols.remove(number)
                for row in puzzle:
                    if row[coord[1]] in sols:
                        sols.remove(row[coord[1]])
                for row in puzzle[3*int(coord[0]/3):3*(int(coord[0]/3)+1)]:
                    for number in row[3*int(coord[1]/3):3*(int(coord[1]/3)+1)]:
                        if number in sols:
                            sols.remove(number)
                if len(sols) == 1:
                    puzzle[coord[0]][coord[1]] = sols[0]
    return puzzle

for row in solve(grid[0]):
    print(row)
