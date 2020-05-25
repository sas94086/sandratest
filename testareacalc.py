# An example to find area of a triangle using a version of Heron's formula
import math

def calcarea(a,b,c):
	# The three arguments are typecast, as they are initially strings
	Area = area_triangle(a,b,c)
	print("The area is:  %f" % Area)
	
	
# Calculate the area 
# Adding an additional line to trigger a build
# Adding an additional line to trigger a build
def area_triangle(a,b,c):
    A = (1.0/4.0) * math.sqrt(
        2*(a**2 * b**2 + a**2 * c**2 + b**2 * c**2) -
        (a**4 + b**4 + c**4) )
    return A
 
if __name__=='__main__':
	#The arguments come from the user
	a = 8.0
	b = 8.0 
	c = 8.0 
	calcarea(a,b,c)  

