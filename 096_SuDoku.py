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
            if digit == '0':
                grid[i][j].append(list(range(1,10)));
            else:
                grid[i][j].append([int(digit)])
        j += 1
    elif line != '\n':
        grid.append([])
        i += 1
        j = 0

def solved(puzzle):
    ''' Check if puzzle (2D-List) is in a solved state '''
    if puzzle == None:
        return False
    for row in puzzle:
        for number in row:
            if len(number) != 1:
                return False
    for (i,j) in [(i,j) for i in range(9) for j in range(9)]:       
        for k in range(9):
            if puzzle[i][j] == puzzle[i][k] and k != j:
                return False
            if puzzle[i][j] == puzzle[k][j] and k != i:
                return False
        for k in range(3*int(i/3),3*(int(i/3)+1)):
            for m in range(3*int(j/3),3*(int(j/3)+1)):
                if puzzle[i][j] == puzzle[k][m] and k != i and j != m:
                    return False
    return True

def simpleSolve(puzzle):
    prevState = copy.deepcopy(puzzle)
    while not solved(puzzle):                                             
#For each unsolved space, find all numbers that would fit and store them in 
#solutions[(row,col)]. If there is only one option, insert it into puzzle.
        for (i,j) in [(i,j) for i in range(9) for j in range(9)]:       
            if len(puzzle[i][j]) > 1:
                sols = list(range(1,10))
                for number in puzzle[i]:
                    if len(number) == 1 and number[0] in sols:
                        sols.remove(number[0])
                for row in puzzle:
                    if len(row[j]) == 1 and row[j][0] in sols:
                        sols.remove(row[j][0])
                for row in puzzle[3*int(i/3):3*(int(i/3)+1)]:
                    for number in row[3*int(j/3):3*(int(j/3)+1)]:
                        if len(number) == 1 and number[0] in sols:
                            sols.remove(number[0])
                puzzle[i][j] = sols
            if len(puzzle[i][j]) == 0:
                return None
#If a pair of locations in a row, col, or quad share a pair of solutions,
#remove that option from the rest of the row, col, or quad.
        for i in range(9):
            for j in range(9):
                if len(puzzle[i][j]) == 2:
                    for x in [a for a in range(9) if a != j]:
                        if puzzle[i][j] == puzzle[i][x]:
                            for y in [a for a in range(9) if a != j and a != x]:
                                for number in puzzle[i][j]:
                                    if number in puzzle[i][y]:
                                        puzzle[i][y].remove(number)
        for i in range(9):
            for j in range(9):
                if len(puzzle[j][i]) == 2:
                    for x in [a for a in range(9) if a != j]:
                        if puzzle[j][i] == puzzle[x][i]:
                            for y in [a for a in range(9) if a != j and a != x]:
                                for number in puzzle[j][i]:
                                    if number in puzzle[y][i]:
                                        puzzle[y][i].remove(number)
        for i in [(a,b) for a in range(3) for b in range(3)]:
             for j in [(a,b) for a in range(3 * i[0], 3 * (i[0]+1)) for b in range(3 * i[1], 3 * (i[1]+1))]:
                 if puzzle[j[0]][j[1]] == 2:
                     for x in [(a,b) for a in range(3 * i[0], 3 * (i[0]+1)) for b in range(3 * i[1], 3 * (i[1]+1)) if (a,b) != j]:
                         if puzzle[j[0]][j[1]] == puzzle[x[0]][x[1]]:
                             for y in [(a,b) for a in range(3 * i[0], 3 * (i[0]+1)) for b in range(3 * i[1], 3 * (i[1]+1)) if (a,b) != j and (a,b) != x]:
                                 for number in puzzle[j[0]][j[1]]:
                                     if number in puzzle[y[0]][y[1]]:
                                         puzzle[y[0]][y[1]].remove(number)
#If any empty location is the only possible location in it's row, column, or 
#quadrant for a certain number, fill it with that number.    
        for i in range(9):
            for number in range(9):
                count = 0
                location = (i,-1)
                for j in range(9):
                    if number in puzzle[i][j]:
                        count += 1
                        location = (i,j)
                if count == 1:
                    puzzle[location[0]][location[1]] = [number]
        for i in range(9):
            for number in range(9):
                count = 0
                location = (-1,i)
                for j in range(9):
                    if number in puzzle[j][i]:
                        count += 1
                        location = (j,i)
                if count == 1:
                    puzzle[location[0]][location[1]] = [number]
        for x in [(a,b) for a in range(3) for b in range(3)]:
            for number in range(9):
                count = 0
                location = (-1,-1)
                for y in [(a,b) for a in range(3 * x[0], 3 * (x[0]+1)) for b in range(3 * x[1], 3 * (x[1]+1))]:
                    if number in puzzle[y[0]][y[1]]:
                        count += 1
                        location = y
                if count == 1:
                    puzzle[location[0]][location[1]] = [number]
#If no progress has been made in one loop, make a guess and get recursive 
        if prevState == puzzle:
            for (i, j) in [(i, j) for i in range(9) for j in range(9)]:
                if len(puzzle[i][j]) > 1:
                    for a in puzzle[i][j]:
                        sub = copy.deepcopy(puzzle)
                        sub[i][j] = [a];
                        sub = simpleSolve(sub)
                        if solved(sub):
                            return sub
                    return None
        prevState = copy.deepcopy(puzzle)
    return puzzle    

#Count the number of puzzles that can currently be solved
total = 0
for x in grid:
    a = simpleSolve(x)
    for row in a:
        print(row)
    print(a[0][0][0] * 100 + a[0][1][0] * 10 + a[0][2][0])
    print()
    total += a[0][0][0] * 100 + a[0][1][0] * 10 + a[0][2][0]
print(total)
