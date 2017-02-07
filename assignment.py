import sys
cmd = sys.argv[1]
    
import numpy as np
import matplotlib.pyplot as plt

xval = np.arange(-3.0, 3.0, 0.1)

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
elif cmd == '4':
    yval = np.sin(xval)
    #print yval
    plt.plot(xval, yval)
    plt.show()
elif cmd == '5':
    yval = np.cos(xval)
    #print yval
    plt.plot(xval, yval)
    plt.show()
if cmd == '6':
    yval = np.tan(xval)
    #print yval
    plt.plot(xval, yval)
    plt.show()
if cmd == '7':
    yval = np.exp(xval)
    plt.plot(xval, yval)
    plt.show()
if cmd == '8':
    yval = np.sqrt(abs(xval))
    plt.plot(xval, yval)
    plt.show()
else:
    print "Usage: Enter '1' to use the lambda function x to populate yval"
    print "Usage: Enter '2' to use the lambda function x**2 to populate yval"
    print "Usage: Enter '3' to use the lambda function x**3 to populate yval"
    print "Usage: Enter '4' to use the sin function to populate yval"
    print "Usage: Enter '5' to use the cos function to populate yval"
    print "Usage: Enter '6' to use the tan function x to populate yval"
    print "Usage: Enter '7' to use the exp  function  to populate yval"
    print "Usage: Enter '8' to use the sqrt(abs(x)) functions  to populate yval"
    
