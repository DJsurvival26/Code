import random 
import numpy as np 
from numpy.polynomial import Polynomial as poly
import sys
def ction(size=4):
    if(size<= 1):
        print("You must include at least 1 argument(number of random array)")
        return -1
    coef=np.random.rand(1,size)
    coef=coef.squeeze()
    return poly(coef)

print(ction(333))
