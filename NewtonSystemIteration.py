import numpy as np
import scipy.linalg

def NewtSysSolve(f,Df,x0,epsx,epsf,itmx):                      # Newton-Raphson iteration for systems of nonlinear equations

    conv = False                                               # Set convergence flag
    err=np.ones(itmx)
    res=np.ones(itmx)
    x = x0                                                     # Sets starting point as initial guess x0
    
    for k in range(0,itmx):                                    # Loop over Newton-Raphson iterates
        
        r_vec = -f(x)                                          # Compute residual vector
        res[k] = scipy.linalg.norm(r_vec,2)                    # Compute residual
        J = Df(x)                                              # Compute Jacobian
        
        dx = scipy.linalg.solve(J,r_vec)                        # solve system J dx = -f

        err[k] = scipy.linalg.norm(dx,2)                       # Estimate of error
        
        print("Iter. " + str(k) + " err= " + str(err[k]) + " res= " + str(res[k]) )    # Print error and residual
        
        x = x + dx                                             # Apply update step
        
        if res[k] < epsf and err[k] < epsx:                    # Test for convergence
            conv = True
            its = k+1
            print("Converged, exiting...")
            break


    if conv==False:
        print("No convergece!")
        its=itmx

    return x,err,res,its


