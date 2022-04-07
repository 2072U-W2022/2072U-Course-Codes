import numpy as np
from NewtonSystemIteration import NewtSysSolve
import matplotlib.pyplot as plt          # For plotting 

def f(x):                                       #  defines the function 
    x1 = x[0]
    x2 = x[1]
    f1=2.0*np.exp(x1*x2) - 2.0*x1 + 2.0*x2 - 2.0
    f2=x1**5 + x1*x2**5 - 2.0*x2
    fval = np.array([f1,f2])
    return fval

def Df(x):                                      #  defines the Jacobian
    x1 = x[0]
    x2 = x[1]    
    J11 = 2.0*np.exp(x1*x2)*x2 - 2.0
    J12 = 2.0*np.exp(x1*x2)*x1 + 2.0
    J21 = 5.0*x1**4 + x2**5
    J22 = 5.0*x1*x2**4 - 2.0
    Jac = np.array([[J11,J12],[J21,J22]])
    return Jac


# Parameters of Newton iteration
epsf = 1.0e-9
epsx = 1.0e-12
itmx = 10
# Initial point
x0 = np.ones((2,1))

#  call Newton iteration function NewtSysSolve defined in NewtonSystemIteration.py
x, err, res, its = NewtSysSolve(f,Df,x0,epsx,epsf,itmx)

print('\n')
print("Note the quadratic convergence!")
print('The solution is: \n'+str(x))
print('\n')


print("Note the solution is not [0,0] as expected.  \n Try a different guess to see if you get the zero solution instead")

plt.figure
plt.semilogy(range(0,its),err[0:its],'-*k')
plt.semilogy(range(0,its),res[0:its],'-*r')
plt.xlabel('Nr. of iterations')
plt.ylabel('residual (red) and error (black)')
plt.title('Convergence for 2 x 2 test problem')
plt.show()


