import time

#Start Timer
init_Time = time.clock()

#Open the file, convert it to a list
matrix = open('081_matrix.txt').read().split()
for i in range(len(matrix)):
    matrix[i] = list(map(int,matrix[i].split(',')))

#Start with the lower right square, and add it's value to each square to the
#above and to the left of it. If 2 squares attempt to add their value to the
#same new square, the old square with the lowest value wins. 
adjacent = [(len(matrix)-2,len(matrix)-1),(len(matrix)-1,len(matrix)-2)]
while len(adjacent) > 0:
    new_adj = []
    for coord in adjacent:
        min_neighbor = 2**31
        if coord[1]+1 < len(matrix):
            min_neighbor = matrix[coord[0]][coord[1]+1]
        if coord[0]+1 < len(matrix) and matrix[coord[0]+1][coord[1]] < min_neighbor:
            min_neighbor = matrix[coord[0]+1][coord[1]]
        matrix[coord[0]][coord[1]] += min_neighbor
        if (coord[0]-1,coord[1]) not in new_adj and coord[0] - 1 >= 0:
            new_adj.append((coord[0]-1,coord[1]))
        if (coord[0],coord[1]-1) not in new_adj and coord[1] - 1 >= 0:
            new_adj.append((coord[0],coord[1]-1))
    adjacent[:] = new_adj 

print(matrix[0][0])
print("Solved in " + str(time.clock() - init_Time) + " seconds")  
