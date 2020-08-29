from sympy import *

if __name__ == "__main__":
    init_printing() 

    x, y, z = symbols('x y z')
    pprint(Integral(sqrt(1/x), x))
