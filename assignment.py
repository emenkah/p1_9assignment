import sys
cmd = sys.argv[1]
    
import numpy as np
import matplotlib.pyplot as plt

xval = np.arange(-5.0, 5.0, 0.1)

if cmd == '1':
    f = lambda x:x
    yval = f(xval)
    #print yval
    plt.plot(xval, yval)
    plt.show()
if cmd == '2':
    f = lambda x:x**2
    yval = f(xval)
    #print yval
    plt.plot(xval, yval)
    plt.show()
if cmd == '3':
    f = lambda x:x**3
    yval = f(xval)
    ########print yval
    plt.plot(xval, yval)
    plt.show()
else:
    print "yval will be populated by some other funtion"
