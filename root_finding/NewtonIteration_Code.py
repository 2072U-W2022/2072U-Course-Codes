
# Python function for Newton iteration
import numpy as np
import matplotlib.pyplot as plt

def NewtonIteration(func, dfunc, x0, kMax, epsX, epsF):
# Input: initial point, max nr. of iterations, tolerance for error and residual
    x=x0
    conv=0
    err=np.ones([kMax,1])                         # flag for convergence
    for k in range(1,kMax):
        fx=func(x)                 # current function value
        dx=-fx/dfunc(x)            # update step
        err[k-1] = abs(dx)              # current error estimate
        res = abs(fx)              # current residual
        print("Iteration "+str(k)+" err="+str(err[k-1])+" res="+str(res))        
#        print 'Iteration %d: approximation is %e, err=%e res=%e\n' % (k,x,err,res)
        if err[k-1] < epsX and res < epsF:       # If converged ...
            print("Converged!")
            conv=1
            break
        x=x+dx
    
    if conv==0:
        print("No convergence!")
    return x,err,res, k

#def func(x):
#    return (x-np.cos(x))*(x-np.cos(x))
    
#def dfunc(x):
#    return 2*(x-np.cos(x))*(1+np.sin(x))

def func(x):
    return np.exp(-x*x)-x
    
def dfunc(x):
    return -2*x*np.exp(-x*x)- 1

x0 = 1.0
x, err, res, num_its = NewtonIteration(func,dfunc,x0,1000,1e-14,1e-4)

print(x, err[num_its-1], num_its)

fig1 = plt.figure(1)
kk = range(num_its)
plt.semilogy(kk, err[kk])
plt.xlabel('number of iterations')
plt.ylabel('approximate error')
plt.title('Newton Iterations for $f(x)=e^{-x^2}-x=0$')
fig1.savefig('fig1.pdf')
plt.show()