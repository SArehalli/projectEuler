import copy

#Convert the data in the puzzles file into a 3-dimensional list called grid[puzzle #][row #][Col #]
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

#Check if puzzle (2D-List) is in a solved state
def solved(puzzle):
    for row in puzzle:
        for number in row:
            if number == 0:
                return False
    return True

def simpleSolve(puzzle):
#For each unsolved space, find all numbers that would fit and store them in 
#solutions[(row,col)]. If there is only one option, insert it into puzzle.
    solutions = {}
    prevState = copy.deepcopy(puzzle)
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
                solutions[coord] = [puzzle[coord[0]][coord[1]]]
#If a pair of locations in a row, col, or quad share a pair of solutions,
#remove that option from the rest of the row, col, or quad.
        for i in range(9):
            for j in range(9):
                if len(solutions[(i,j)]) == 2:
                    for x in [a for a in range(9) if a != j]:
                        if solutions[(i,j)] == solutions[(i,x)]:
                            for y in [a for a in range(9) if a != j and a != x]:
                                for number in solutions[(i,j)]:
                                    if number in solutions[(i,y)]:
                                        solutions[(i,y)].remove(number)
        for i in range(9):
            for j in range(9):
                if len(solutions[(j,i)]) == 2:
                    for x in [a for a in range(9) if a != j]:
                        if solutions[(j,i)] == solutions[(x,i)]:
                            for y in [a for a in range(9) if a != j and a != x]:
                                for number in solutions[(j,i)]:
                                    if number in solutions[(y,i)]:
                                        solutions[(y,i)].remove(number)
        for i in [(a,b) for a in range(3) for b in range(3)]:
            for j in [(a,b) for a in range(3 * i[0], 3 * (i[0]+1)) for b in range(3 * i[1], 3 * (i[1]+1))]:
                if solutions[j] == 2:
                    for x in [(a,b) for a in range(3 * i[0], 3 * (i[0]+1)) for b in range(3 * i[1], 3 * (i[1]+1)) if (a,b) != j]:
                        if solutions[j] == solutions[x]:
                            for y in [(a,b) for a in range(3 * i[0], 3 * (i[0]+1)) for b in range(3 * i[1], 3 * (i[1]+1)) if (a,b) != j and (a,b) != x]:
                                for number in solutions[j]:
                                    if number in solutions[y]:
                                        solutions[y].remove(number)

#If any empty location is the only possible location in it's row, column, or 
#quadrant for a certain number, fill it with that number.    
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
#If no progress has been made in one loop, return None
        if prevState == puzzle:
            return None
        prevState = copy.deepcopy(puzzle)
    return puzzle    

#Count the number of puzzles that can currently be solved
num = 0
for puzzle in grid:
    if simpleSolve(puzzle) != None:
        num += 1
print(num)
