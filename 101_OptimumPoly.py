import numpy as np
U_n = [1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10 for n in range(1,21)]
#U_n = [n**3 for n in range(1,6)]

def OP(k, seq):
    mat = np.matrix([[x**n for n in range(k-1, -1, -1)] for x in range(1,k+1)])
    sol = np.matrix([[x] for x in seq[:k]])
    coef = mat.getI() * sol
    f = lambda x: sum([m * x**(k-1-ind) for ind,m in enumerate(coef)])[0,0] 
    return f

errorSum = 0
z = 1
while(abs(OP(z,U_n)(z+1) -  U_n[z]) > 0.00001*U_n[z] ):     # NumPy Precision!
    errorSum += OP(z, U_n)(z+1)                             # But hey, Matrices are hard
    z += 1                                                  # 
print(int(errorSum+1))                                      # int(errorSum + 1) 
