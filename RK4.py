from math import *

def rk(f, x0, y0, xn, h):
    k = 0
    print('k | xk | yk | k1 | k2 | k3 | k4')

    xk = x0
    yk = y0
    
    while True:

        k1 = f(xk, yk)
        k2 = f(xk + h/2, yk + (h / 2) * k1)
        k3 = f(xk + h/2, yk + (h / 2) * k2)
        k4 = f(xk + h, yk + h * k3)

        print('{} | {:.1f} | {:.6f} | {:.6f} | {:.6f} | {:.6f} | {:.6f}'.format(k, xk, yk, k1, k2, k3, k4))
        k += 1
        xk = xk + h
        yk = yk + (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)

        if xk > xn:
            break


