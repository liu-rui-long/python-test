import math
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-6))

def quadratic(a,b,c):
    delta=b**2-4*a*c
    if delta<0:
        return None
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return x1,x2
print(quadratic(2,3,1))
