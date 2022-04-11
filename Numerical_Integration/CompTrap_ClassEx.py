import numpy as np
import matplotlib.pyplot as plt


def comp_trap(f,a,b,M):
    xs = np.linspace(a,b,M+1)
    h = (b-a)/float(M)
    I = (f(a)+f(b)) / 2.0
    for i in range(1,M):
        I = I + f(xs[i])
    I = h * I
    return I

def f(x):
    return np.sqrt(1.0+x**4)

a = 0.0
b = 1.0
Mtest = 15
M = 2
h = (b - a)/float(M)

h_all = np.zeros(Mtest)
Error_all = np.zeros(Mtest)

I_final = comp_trap(f,a,b,M**(Mtest+2))
print(I_final)


for i in range(Mtest):
    M = M * 2
    h = (b -a)/float(M)
    Itrap = comp_trap(f,a,b,M)
    print('The approximation is '+str(Itrap)+' with '+str(M)+' subintervals')
    h_all[i]= h
    Error_all[i] = (comp_trap(f,a,b,M)-I_final)


plt.loglog(h_all,Error_all)
plt.title('$O(h^2)$ Error using composite trapezoidal rule')
plt.xlabel('h')
plt.ylabel('approximate error')
plt.show()
