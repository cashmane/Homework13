import numpy as np
import matplotlib.pyplot as plt

def dist():
    '''Returns a random sample from the distribution 1/(2*sqrt(x))'''
    x = np.random.random()
    return x**2

def impsamp(N):
    '''Performs integration through importance sampling
        Takes in N which is the number of points to evaluate the integral.'''
    total = 0 
    for i in range(N):
        x = dist()
        val = (1/(np.exp(x)+1))*2 #importance sampling formula
        total += val #adds this point to the total
    total = total/N 
    return total
        
if __name__ == '__main__':
    N = int(1e6) #evaluate 1 million points
    integral = impsamp(N)
    print('The solution to the integral is', integral)
    
