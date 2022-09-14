# logs.py
#must be (-10,7]
# Outputs the value of g(x) = ln(100-x^2) + sqrt(84 - 5x - x^2) at the input x-value.

import math

#functions
def g(x):
    return math.log(100 - x**2) + math.sqrt(84 - 5*x - x**2)

#inputs + convert to float
x = input("Input the value for x: ")
x = float(x)

#checking correct value
if x <= -10 or x > 7 :
    print("Input not valid, please try again.")
    exit()
elif x:
    print("g(" + str(x) + ") = " + str(g(x)))


#print("g(" + str(x) + ") = " + str(g(x)))
