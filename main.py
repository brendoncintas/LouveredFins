import math
import numpy as np


# Main script handles all of the calculations and plots the results using scipy.

# 1. Declaration of the ranges for the calculations:

numBiot = [1e-4, 1e-5, 1e-6]
numPhi = [3.33, 2, 1.67] # Ratio of convection coefficients
numOmega = [0.1,0.2,0.3,0.5,0.7,0.9] # Ratio of b1/b
numAlpha = [200,140,80] # ratio of c/t
numGamma = [1.5,1.0,0.5] # ratio of b/c
numBeta1 = [0.5,0.6,0.7,0.8,0.9,0.95] # Ratio of c1/c
numBeta2 = [0.25,0.45,0.75] # Ratio of b2/b

