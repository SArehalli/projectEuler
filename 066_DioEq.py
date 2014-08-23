import math
import fractions
import time
 
def frac(a):
    """ Convert continued fraction notation to decimal notation"""
    if len(a) < 2: 
        return a[0]
    pa = a[0]
    pb = a[0] * a[1] + 1
    for i in range(2, len(a)):
        pc = pa + (pb * a[i])
        pa = pb
        pb = pc
    return pb

def contFracMethod(D):
    """ Apply the continued fraction method to solve the 2nd order Dio Eq """
    b=[]
    b.append(math.floor(math.sqrt(D)))
    p = 0
    q = 1
    p = b[0] * q - p
    q = (D - p**2) / q
    b.append(math.floor((p + math.sqrt(D)) / q))
    n = 0
    while b[-1] != 2*b[0]:
       n += 1
       p = b[n] * q - p
       q = (D - p**2) / q
       b.append(math.floor((p + math.sqrt(D)) / q))
    b.pop()
    if len(b) % 2 == 0:
        return frac(b)
    else:
        return frac(b + [2*b[0]] + b[1:] + [2*b[0]])

#Start Timer
init_Time = time.clock()
#Find the largest minimum solution for D <= 1000 
key = 0
ma = 0
for D in [x for x in range(1001) if math.floor(math.sqrt(x)) != math.sqrt(x)]:
    a  = contFracMethod(D)    
    if a > ma:
        ma = a
        key = D
print(key)
print("Solved in " + str(time.clock() - init_Time) + " seconds.")

