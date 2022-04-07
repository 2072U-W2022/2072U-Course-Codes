#  examples of piece-wise polynomial interpolation

import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
from scipy.interpolate import PchipInterpolator
from scipy.interpolate import UnivariateSpline

#  enter data points
#x = np.array([0, 1.2, 1.9, 2.3, 3.2, 4.1])
#y = np.array([0, 2.2, 1.1, 3.6, 1.1, 5.1])

# data
x = np.linspace(0,10,15)
y = np.cos(-x**2/9.0)

#  points for plotting
xx = np.linspace(0,10,1000)
# for plotting the original function
yy = np.cos(-xx**2/9.0)

# piecewise linear interpolation
#f_lin = interp1d(x,y)

# cubic spline interpolation
f_cub = CubicSpline(x,y)

# compute first derivative of cubic spline
#f_cub=f_cub.derivative()

# shape-preserving cubic interpolation
#f_pchip = PchipInterpolator(x,y)

# compute first derivative of the interpolant
#f_cub = f_pchip.derivative()

# Also cubic interpolation (using a more general function)
#f_uni = UnivariateSpline(x,y,k=3,s=0)

# compute first derivative of the cubic spline
#fd1 = f_uni.derivative()


plt.plot(x,y, 'o',xx, yy,'-r',xx,f_cub(xx),'-b')
plt.legend(['data','f','cubic'])
plt.show()