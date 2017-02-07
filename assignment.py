import sys
cmd = sys.argv[1]
    
import numpy as np
import matplotlib.pyplot as plt

xval = np.arange(-5.0, 5.0, 0.1)

if cmd == '1':
    f = lambda x:x
    yval = f(xval)
    plt.plot(xval, yval)
    plt.show()
if cmd == '5':
    yval = np.exp(xval)
    plt.plot(xval, yval)
    plt.show()
if cmd == '6':
    yval = np.sqrt(abs(xval))
    plt.plot(xval, yval)
    plt.show()
else:
    print "Usage: Enter '1' to use the lambda function x to populate yval"
    print "Usage: Enter '5' to use the exp  function  to populate yval"
    print "Usage: Enter '6' to use the sqrt(abs(x)) functions  to populate yval"
    



