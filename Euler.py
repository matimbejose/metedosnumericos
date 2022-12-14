from math import *

def e(f, x0, y0, xn, h):
    k = 0
    print('k | xk | yk')

    xk = x0
    yk = y0
    
    while True:
        print('{:.5f} | {:.5f} | {:.5f}'.format(k, xk, yk))

        xk = xk + h
        yk = yk + h * (f(xk, yk))
        k += 1

        if xk > xn:
            break

