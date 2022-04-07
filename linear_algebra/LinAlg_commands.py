#  


import numpy as np
#import scipy.linalg
import scipy

A = np.array([[-7,-5,3],[-1,-8,2]])
# or
#A = np.mat('[-7,-5,3;-1,-8,2]')

print('The matrix A=')
print(A) 
print('\n')

a13 = A[0,2]
#or 
a13 = A[0][2]

print('The component a_1,3 of A = '+str(a13)+'\n' )


# find the transpose of A
B = A.T
#  or
B = scipy.transpose(A)


print('The transpose of A is =')
print (B)
print('\n')


#  sum of matrices  (dimension must be the same)
C=scipy.add(A,2*A)
# or
C = A + 2*A

print('The sum of A and 2A is =')
print (C)
print('\n')

#  multipy two matrices  (dimensions must be such that this is defined)
C = scipy.matmul(A,B)
# or
C = scipy.dot(A,B)  # this is not preferred 
#or
C = A @ B

print('Are dimensions for product right?')
print(np.shape(A)[1]==np.shape(B)[0])
print('\n')


print('The product of A and A transpose is =')
print (C)
print('\n')

#  solve A x = b

A = np.array([[-7,-5],[-1,-8]])
b = np.array([[1],[3]])

xx = scipy.linalg.solve(A,b)

print('Solving A x = b...')
print('x=')
print(xx)
print('\n')

#  find the inverse of A
Ainv = scipy.linalg.inv(A)

#  find the determinant of A
d =  scipy.linalg.det(A)


print('The inverse of A = ' )
print(Ainv)
print('\n')

print('The det of A = '+str(d))
print('\n')

#  the identity matrix
Id=np.identity(4)

#  the zero matrix
Zmat=np.zeros((3,3))

print('the identity matrix')
print(Id)
print(' and the zero matrix')
print(Zmat)
print('\n')


#  the first unit vector
e1 = Id[:,[0]]

print('The first unit fector is')
print(e1)
print('\n')


