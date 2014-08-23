import time

#Start Timer
init_Time = time.clock()

#Do the thing. 
M = 0 
Cuboids = 0
while Cuboids < 1000000:
    M += 1
    for x in [(M,b) for b in range(2, 2*M+1)]:   
        d = (x[0]**2 + (x[1])**2)**(0.5)
        if int(d) == d:
            if x[1] <= M+1:
                Cuboids += int(x[1]/2)
            else:
                Cuboids += int((2*M+2-x[1])/2) 
            if Cuboids > 1000000:
                break

print(M)
print("Solved in " + str(time.clock() - init_Time) + " seconds")
