## Brendon Cintas - 6158218 ##
## EML 5152 - Intermediate Heat Transfer ##

## Unlouvered ##

import math
import numpy as np

# Unlouvered section of the 2D model addressed in Optimization of Louvered Fins in Intermittent Contact with Plate Heat Exchanger Passageways by J.G. Burgers and T.F. Lemczyk from Ontario, Canada looked at the heat exchange within the fin in which no Louvers are present. There are two sections where Louvers are not present: sector 4 (a and b), and sector 1.

# Sector 1

# Assumptions: 1. Element of uniform temperature acting at centroid. Heat is conducted into the element from its contacting boundary with the source which is at uniform temperature, through resistance.

def sector1(numBiot, numAlpha, numBeta1, numOmega, numGamma):
    global R1B, R1S, R13

    # Thermal Resistance of sector 1B. 
    R1B = (1-numBeta1)/(2*numOmega*numGamma)
    # Some of the heat is convected directly into the sink through resistance
    R1S = 1/(numBiot*(numAlpha**numAlpha)*numOmega(1-numBeta1)*numGamma)
    # Some heat is conducted to the border with sector 2 through resistance R*1b and to the border with sector 3 through resistance
    R13 = (numOmega*numGamma)/(2*numBiot)

