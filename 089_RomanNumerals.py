import time

#Start Timer
init_Time = time.clock()

#initialize things
num = { 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
chars = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
denoms = [1000, 500, 100, 50, 10, 5, 1]


#Open the file and record the initial length
f = open('089_roman.txt').read()
init_Length = len(f)
roman = f.split()

def toInt(numeral):
    ''' Convert a roman numeral to an integer '''
    integer = 0
    for i in range(len(numeral)):
        if i == len(numeral) - 1 or num[numeral[i]] >= num[numeral[i+1]]:
            integer += num[numeral[i]]
        else: 
            integer -= num[numeral[i]]
    return integer

def number_Of(target, numeral):
    sol = []
    for i in range(len(numeral)):
        if numeral[i] == target:
            sol.append(i)
    return sol

def toRoman(integer):
    '''convert an integer to a roman numeral '''
    numeral = ""

    #Convert the integer to a primative Roman numeral.
    for i in range(len(denoms)):
        x = integer / denoms[i]
        integer = integer % denoms[i]
        numeral += int(x) * chars[i]

    #Convert the primative Roman numeral into the optimal Roman numeral
    for i in range(len(chars)-1, 0, -1):
        pos = number_Of(chars[i], numeral)
        if i % 2 == 0:
            if len(pos) == 4 and pos[3] - pos[0] == 3:
                numeral = numeral[:pos[0]] + numeral[int((pos[0]+pos[1])/2)] + chars[i-1] + numeral[pos[-1]+1:]
            if len(pos) == 5 and chars.index(numeral[pos[-1]-1]) - i < 2: 
                numeral = numeral[:pos[0]] + numeral[pos[-1]-1] + chars[i-1] + numeral[pos[-1]+1:]
            elif len(pos) == 5:
                numeral = numeral[:pos[0]] + numeral[int((pos[0]+pos[1])/2)] + chars[i-1] + numeral[pos[-2]+1:]
        else:
            if len(pos) == 2 and chars.index(numeral[pos[-1]-1]) - i < 2: 
                numeral = numeral[:pos[0]] + numeral[int((pos[0]+pos[1])/2)] + chars[i-1] + numeral[pos[-1]+1:]
    return numeral

#Reformat into one multiline string
solution = ""
for line in roman:
    solution += toRoman(toInt(line)) + "\n" 

print(init_Length - len(solution) + 1)
print("Solved in " + str(time.clock() - init_Time) + " seconds")
