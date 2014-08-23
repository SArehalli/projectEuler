import time

#Start Timer
init_Time = time.clock()

#Convert the data file into a list
f = open('079_keylog.txt','r')
data = [int(line) for line in f]

graphout = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 0:[]}
graphin = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 0:[]}

#Create 2 dicts filled with numbers that must go before/after the key
for x in data:
    for n in range(0, 2):
        if not int(str(x)[n+1]) in graphout[int(str(x)[n])]:
            graphout[int(str(x)[n])].append(int(str(x)[n+1]))
        if not int(str(x)[n]) in graphin[int(str(x)[n+1])]:
            graphin[int(str(x)[n+1])].append(int(str(x)[n]))

#Remove all numbers that are not present in the dataset
for key in range(0, 10):
    if len(graphout[key]) == 0 and len(graphin[key]) == 0:
        graphin.pop(key, None) 
        graphout.pop(key, None) 

#Create the password from the graph. 
Password = []
while len(graphin) != 0:
	for key in graphin:
		if len(graphin[key]) == 0:
			Password.append(key)
			break
	graphin.pop(Password[-1], None)
	for key in graphin:
		if Password[-1] in graphin[key]:
			graphin[key].remove(Password[-1])

print(Password)
print("Solved in " + str(time.clock() - init_Time) + " seconds")
