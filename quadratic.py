#QUADRATIC EQUATION ---

#1/usr/bin/python
##########################
##########################


#A is the coeficient of the first term
#B is the co eficient of the second term
#C is the constant

#from cmath import sqrt
import math

a = int(input("enter the coeficient of the first term"))
b = int(input("enter the coeficient of the second term"))
c = int(input("enter the constant"))
w = math.sqrt((b**2) - 4*a*c)
def first_root (a,b,c):
    y_1 =( -b + w) / (2*a)
    y_2 =( -b - w) / (2*a)
    print("the roots of the quadratic equation are :",y_1,y_2)

first_root (a,b,c)      