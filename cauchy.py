import numpy as np
import matplotlib.pyplot as plt

def random_cauchy(N, x0, gamma):
    '''Returns a list of random point from Cauchy distribution.
        N: number of points to return.
        x0: mean of the distribution
        gamma: scale factor for width of distribution'''
    retList = []
    ranList = []
    for i in range(N):
        y = np.random.uniform(0, 1)
        ranList.append(y) #appends the initial random value between 0 and 1 to a list.
        val = (gamma*np.tan(np.pi*(y-0.5)))+x0 #inverse cdf
        retList.append(val) #appends the random value from distribution to a list.
    return ranList, retList #returns a list of the initial random number, and a list of the transformed random numbers.

def pdf(x, x0, gamma):
    '''Probability distribution funtion.
        x - number to evaluate
        x0 - mean of the distribution
        gamma - scalar for width of distribution.'''
    return 1/(np.pi*gamma*(1+(x-x0/gamma)**2))
 
if __name__ == '__main__':
    gamma = 1
    xs = np.arange(-40, 40, 0.1)
    ys = pdf(xs, 0, gamma)
    randList, valList = random_cauchy(10000, 0, gamma)

    
    plt.plot(xs, ys, label='PDF') #plot the PDF
    plt.hist(valList, bins=xs, density=True, #plot the random samples from dist
             label='Samples from inverse CDF',
             alpha=0.5)
    plt.xlim(-40, 40)
    plt.xlabel("X")
    plt.ylabel('Density')
    plt.title('Cauchy distribution, x0=0, Gamma=1')
    plt.legend()
    plt.show()
    #plt.savefig('cauchy.png')
    
