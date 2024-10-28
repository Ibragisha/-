from cmath import atanh
import math
a=6378137.0
c=6356752.314245
e=1-(c**2/a**2)
s=2*math.pi*a**2*(1+((1-e)/e**0.5)*math.atanh(e**0.5))
print (s)