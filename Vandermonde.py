import numpy as np

def VanderMatrix(xs):
    
    Np1 = xs.shape[0]
    V = np.vander(xs)
    M = np.zeros(V.shape)
    
    
    for j in range(Np1):
        
        M[:,j] = V[:,Np1-j-1]
        
    return M

def MonoPolyEval(a_coeff,xx):  
    
    p = 1
    q = a_coeff[0]
    N = a_coeff.shape[0]
    
    for j in range(1,N):
        p = p*xx
        q = q + a_coeff[j]*p
        
    return q


