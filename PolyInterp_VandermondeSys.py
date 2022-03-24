import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
#from NewtonPolynomial import NewtonPolyBuild
#from NewtonPolynomial import NewtonPolyEval
from Vandermonde import VanderMatrix
from Vandermonde import MonoPolyEval

endpoint = np.pi/2.0
NumIterpPts= 5

x = np.array([0,np.pi/6,np.pi/4,np.pi/3,np.pi/2])
y = np.array([0,1.0/2.0,1.0/np.sqrt(2),np.sqrt(3)/2,1.0])

#x = np.linspace(0,endpoint,NumIterpPts)
xx = np.linspace(0, endpoint, num=100, endpoint=True)

#y = np.sin(x)
#y = np.cos(-x**2/9.0)
yy2 = np.sin(xx)
#yy2 = np.cos(-xx**2/9.0)


#V = NewtonPolyBuild(x)
V = VanderMatrix(x)
a_coeff = scipy.linalg.solve(V,y)


#yy = NewtonPolyEval(a_coeff,x,xx)
yy = MonoPolyEval(a_coeff,xx)


plt.plot(x, y, 'o',xx,yy, '-b', xx, yy2, '--')

plt.legend(['data', 'polynomial interpolant','f(x)'], loc='best')
plt.show()



