import sys
cmd = sys.argv[1]
    
import numpy as np
import matplotlib.pyplot as plt

xval = np.arange(-3.0, 3.0, 0.1)

if cmd == '1':
    f = lambda x:x
    yval = f(xval)
    plt.plot(xval, yval)
    plt.show()
elif cmd == '2':
    yval = np.sin(xval)
    #print yval
    plt.plot(xval, yval)
    plt.show()
elif cmd == '3':
    yval = np.cos(xval)
    #print yval
    plt.plot(xval, yval)
    plt.show()
if cmd == '4':
    yval = np.tan(xval)
    #print yval
    plt.plot(xval, yval)
    plt.show()
else:
    print "Usage: Enter '1' to use the lambda function x to populate yval"
    print "Usage: Enter '2' to use the sin function to populate yval"
    print "Usage: Enter '3' to use the cos function to populate yval"
    print "Usage: Enter '4' to use the tan function x to populate yval"
