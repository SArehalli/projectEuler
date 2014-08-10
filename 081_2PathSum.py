matrix = open('081_matrix.txt').read().split()
for i in range(len(matrix)):
    matrix[i] = list(map(int,matrix[i].split(',')))

adjacent = [(len(matrix)-2,len(matrix)-1),(len(matrix)-1,len(matrix)-2)]
while len(adjacent) > 0:
    newadj = []
    for coord in adjacent:
        LowestNeighbor = 2**31
        if coord[1]+1 < len(matrix):
            LowestNeighbor = matrix[coord[0]][coord[1]+1]
        if coord[0]+1 < len(matrix) and matrix[coord[0]+1][coord[1]] < LowestNeighbor:
            LowestNeighbor = matrix[coord[0]+1][coord[1]]
        matrix[coord[0]][coord[1]] += LowestNeighbor
        if (coord[0]-1,coord[1]) not in newadj and coord[0] - 1 >= 0:
            newadj.append((coord[0]-1,coord[1]))
        if (coord[0],coord[1]-1) not in newadj and coord[1] - 1 >= 0:
            newadj.append((coord[0],coord[1]-1))
    adjacent[:] = newadj 

print(matrix[0][0])  
