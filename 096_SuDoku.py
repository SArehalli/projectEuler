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

'''
    Simple is Harder
    New Techniques create small gains
    But closer beats far

'''

def simpleSolve(puzzle):
    solutions = {}
    prevState = puzzle
    while not solved(puzzle):                                             
        for coord in [(i,j) for i in range(9) for j in range(9)]:       
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
                solutions[coord] = sols
                if len(sols) == 1:
                    puzzle[coord[0]][coord[1]] = sols[0]
            else:
                 solutions[coord] =[puzzle[coord[0]][coord[1]]]
        for i in range(9):
            for number in range(9):
                count = 0
                location = (i,-1)
                for j in range(9):
                    if number in solutions[(i,j)]:
                        count += 1
                        location = (i,j)
                if count == 1:
                    puzzle[location[0]][location[1]] = number
        for i in range(9):
            for number in range(9):
                count = 0
                location = (-1,i)
                for j in range(9):
                    if number in solutions[(j,i)]:
                        count += 1
                        location = (j,i)
                if count == 1:
                    puzzle[location[0]][location[1]] = number
        for x in [(a,b) for a in range(3) for b in range(3)]:
            for number in range(9):
                count = 0
                location = (-1,-1)
                for y in [(a,b) for a in range(3 * x[0], 3 * (x[0]+1)) for b in range(3 * x[1], 3 * (x[1]+1))]:
                    if number in solutions[y]:
                        count += 1
                        location = y
                if count == 1:
                    puzzle[location[0]][location[1]] = number
        if puzzle == prevState:
            break
        prevState = puzzle
    return puzzle    
for puzzle in grid:
    for row in simpleSolve(puzzle):
        print(row)
    print()
