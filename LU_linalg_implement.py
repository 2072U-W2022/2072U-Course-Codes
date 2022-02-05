#  code for using scipy.linalg.lu to solve A x = b
#    uses scipy.linalg.lu to find A = Pt L U, 
#    then uses scipy.linalg.solve_triangular to solve the resulting triangular systems

import scipy
import scipy.linalg
import numpy as np

A = np.array([[0.2,1.4,-0.4,12.3],[-2.3,4.2,1.1,-0.9],[9.2,-2.3,-0.1,2.2],[3.4,3.3,-10.1,4.0]])
b = np.array([[0.2],[-1.2],[3.3],[0.2]])
#  linalg finds Pt, L and U such that A = Pt L U 
#  (Pt is inverse of what we did in class; but for 
#    permutation matrices, inverse of P is transpose of P)
Pt,L,U = scipy.linalg.lu(A)
P = Pt.T
Pb = scipy.matmul(P,b)
y = scipy.linalg.solve_triangular(L,Pb,lower=True)
x = scipy.linalg.solve_triangular(U,y,lower=False)

print('Matrix is\n')
print(A)
print('\n')

print('L=')
print(L)
print('\n')

print('U=')
print(U)
print('\n')

print('P=')
print(Pt.T)
print('\n')

print('Residual vector is\n')
print(scipy.matmul(A,x)-b)
print('\n')

#  Pt L U = A
#print(Pt @ L @ U-A)

#  P A = L U
#print(P @ A - L @ U)
