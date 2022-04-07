
#  Bisection code as programmed in Lecture 3 (by G. Lewis and attending students)
#  Input: function f, starting points a0 and b0,
#    also need max iteration k_max, tolerances eps_x, eps_f

import numpy as np

def bisect(f,a0,b0,k_max,eps_x,eps_f):
    conv = 0                             # flag for convergence, default is "not converged"
    a = a0
    b = b0
    for k in range(k_max):              # loop over at most k_max bisection steps
        c = (a + b)/2.0                 # find the current midpoint
        f_mid = f(c)                    # compute the function value at the midpoint
        f_left=f(a)                     # compute the function value at the current left boundary
        if (f_mid*f_left > 0):          # if they have the same sign...
            a=c                         # update the left boundary, otherwise...
        else:
            b=c                         # update the right boundary
        max_err = abs(b-a)              # compute the maximal error and the residual
        res = abs(f_mid)
        print("iteration %d err=%e and res=%e" % (k+1,max_err,res))   # Since k starts at 0, I added 1 to k to make the first iteration 1

        if (max_err < eps_x) and (res < eps_f):     # if both are less than their tolerance, stop iterations
            conv=1                                  # set the convergence flag to "converged"
            break

    if (conv==0):                                   # print warning if the iterations did not converge
        print("No convergence after %d interations" % (k_max) )

    return c,max_err                    # return the approximate solution and maximal error


def f(x):
    return np.exp(-x*x)-x

a0 = 0.0
b0 = 1.0
k_max=100
eps_x = 1.0e-5
eps_f = 1.0

xstar,err=bisect(f,a0,b0,k_max,eps_x,eps_f)

print("x = %e" % (xstar))
