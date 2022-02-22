import random 
import numpy as np 
from numpy.polynomial import Polynomial as poly
import sys
def ction(size):
    if(size<= 1):
        print("You must include at least 1 argument(number of random array)")
        return -1
    length= random.randrange(2,15,1)
    coef=np.random.rand(1,length)
    coef=coef.squeeze()
    return poly(coef)


