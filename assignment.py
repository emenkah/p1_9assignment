import sys
cmd = sys.argv[1]
    
import numpy as np
import matplotlib.pyplot as plt

xval = np.arange(-5.0, 5.0, 0.1)

if cmd == '1':
    f = lambda x:x
    yval = f(xval)
    print yval
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
    print "yval will be populated by some other funtion"
