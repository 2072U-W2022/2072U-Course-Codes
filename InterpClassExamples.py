import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator
#from scipy.interpolate import barycentric_interpolate

startpoint = 0          #  left endpoint of interval 
endpoint = 10           #  right endpoint of interval
NumIterpPts = 10        #  = N+1 = number of interpolation points 


def f(xs):
    return np.cos(-xs*xs/9.0)

x = np.linspace(startpoint,endpoint,NumIterpPts)    # x coords of data points: equally spaced interpolation points
y = f(x)                                       # y coords of data points: value of function at interp. points

Q_N = BarycentricInterpolator(x, y)                 # Q_N is Python function for interpolating polynomial 


xx = np.linspace(startpoint, endpoint, 100)     #  x points where I want to plot 
yy2 = f(xx)                                     #  values of original function for plotting comparison

yy = Q_N(xx)                                    #  function values of interpoloting polynomial at x values in xx (for plotting)                 

#  This is a 'convenience function' does interpolating and evaluation of interpolant in one go
#yy = barycentric_interpolate(x, y, xx)

plt.plot(x, y, 'o',xx,yy2, '-r',xx,yy, '-b') #, xx, f2(xx), '--')

plt.xlabel('x')
plt.title('Polynomial Interpolation with polynomial of degree '+str(NumIterpPts-1))
plt.legend(['data', 'function','interpolating polynomial'], loc='best')

plt.show()



