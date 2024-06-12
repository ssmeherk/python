##########################################################################
# author: ssmeherk
# date: 12.06.2024
# version: v1
# task/purpose: given a complex number input, convert to polar coordinates
# source: https://www.hackerrank.com/challenges/polar-coordinates/problem
###########################################################################

import cmath

print("Complex Number, z = x+yj where x is real part and y is imaginary part")
print("Please enter a complex number as input (x+yj):")
z = complex(input())                # read the input
x = z.real                          # real part
y = z.imag                          # imaginary part

r = abs(complex(x, y))              # distance
phi = cmath.phase(complex(x, y))    # angle

precision_r = '{0:0.3f}'.format(r)
precision_phi = '{0:0.3f}'.format(phi)

print(precision_r)
print(precision_phi)
