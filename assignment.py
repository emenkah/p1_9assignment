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
    plt.plot(xval, yval)
    plt.show()
else:
    print "Usage: Enter '1' to use the lambda function x to populate yval"
    print "Usage: Enter '2' to use the lambda function x**2 to populate yval"
    print "Usage: Enter '3' to use the lambda function x**3 to populate yval"
