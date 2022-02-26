import numpy as np
import scipy.linalg

v = np.array([1,2,4])
print(np.linalg.norm(v,2))

A=np.array([[1,0],[1,-3]])
print(np.linalg.cond(A,2))

xs = np.linspace(-1,1,21)
#xs = xs.T
#print(np.shape(xs))
V = np.vander(xs)

cond_V =np.linalg.cond(V,2)

print(cond_V)

b = xs - xs*xs

s = scipy.linalg.solve(V,b)

print(s)

r = np.matmul(V,s)-b

print(r)

x_exact = np.zeros(21)
x_exact[19] = 1
x_exact[18] = -1

err = x_exact - s
print(err)

nrm_r = np.linalg.norm(r,2)
nrm_b = np.linalg.norm(b,2)
nrm_err = np.linalg.norm(err,2)
nrm_x = np.linalg.norm(x_exact,2)

print(cond_V)
print(nrm_r)
print(nrm_err)

print(nrm_err/nrm_x)
print(cond_V*nrm_r/nrm_b)
