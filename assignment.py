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
else:
    print "Usage: Enter '1' to use the lambda function x to populate yval"
