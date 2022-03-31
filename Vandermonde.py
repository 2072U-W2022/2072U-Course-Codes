import numpy as np


def VanderMatrix(xs):
    
    Np1 = xs.shape[0]
    V = np.ones((Np1,Np1))
    
    for i in range(Np1):

        for j in range(1,Np1):
            V[i,j] = V[i,j-1]*xs[i]
    
    return V


def MonoPolyEval(a_coeff,xx):  
    
    p = 1
    q = a_coeff[0]
    N = a_coeff.shape[0]
    
    for j in range(1,N):
        p = p*xx
        q = q + a_coeff[j]*p
        
    return q


