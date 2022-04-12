def plug():
    x = -100
    while x < 100:
        if 2*x + 5 == 13:
            print("x =",x)
        x += 1

plug()


def equation(a,b,c,d):
    return (d - b)/(a - c)

print(equation(2,5,0,13))


# polynomials.py
from math import sqrt
def quad(a,b,c):
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2

print(quad(2,7,-15))


# solve cubic equation
def g(x):
    return 6*x**3 + 31*x**2 +3*x - 10

def plug():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x=",x)
        x += 1
    print("done.")
plug()






