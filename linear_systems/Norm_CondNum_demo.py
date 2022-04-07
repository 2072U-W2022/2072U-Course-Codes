import numpy as np
import scipy.linalg

# compute the norm of a vector v
v = np.array([1,2,4])
# l-2 norm
np.linalg.norm(v,2)
# l-1 norm
np.linalg.norm(v,1)
# l-inf norm
np.linalg.norm(v,np.inf)

#  compute the condition number of a matrix A
A=np.array([[1,0],[1,-3]])
np.linalg.cond(A,2)


#  Example of application of condition number

# construct the Vandermonde matrix V with n=20
#    with x_j equally spaced points between -1 and 1
xs = np.linspace(-1,1,21)
V = np.vander(xs)

#  compute the condition number of V
cond_V =np.linalg.cond(V,2)

print('Condition number of V is' + str(cond_V)+'\n')

# construct the right hand side so that solution to Vs = b are known
b = xs - xs*xs

# find approximation to the solutin V s = b
s = scipy.linalg.solve(V,b)

print('The approximate solution of V s = b is:')
print(s)
print('\n')

# compute the residual vector
r = np.matmul(V,s)-b
print('The residual vector is:')
print(r)
print('\n')

# write down the exact solution (see Lecture 7 slides)
x_exact = np.zeros(21)
x_exact[19] = 1
x_exact[18] = -1

# compute the error vector 
err = x_exact - s
print('The error vector is:')
print(err)
print('\n')

# compute the l-2 norms of r, b, err, x_exact
nrm_r = np.linalg.norm(r,2)
nrm_b = np.linalg.norm(b,2)
nrm_err = np.linalg.norm(err,2)
nrm_x = np.linalg.norm(x_exact,2)

print('Condition number of V = ' + str(cond_V))
print('The redisual = '+str(nrm_r))
print('The error = '+str(nrm_err))

#  the error bound given in the notes is nrm_err/nrm_x < cond_V * nrm_r/nrm_b
print('Error/norm of x = ' +str(nrm_err/nrm_x))
print('K(A) residual/norm of b = '+str(cond_V*nrm_r/nrm_b))
print('Error/norm of x < K(A) residual/norm of b is '+str(nrm_err/nrm_x<cond_V*nrm_r/nrm_b))