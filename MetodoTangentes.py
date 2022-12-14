from math import *

def tg(f, ff, x0, erro_max):
    m = 0
    xm = x0

    print('m | xm | xmm | erro')
    while True:
        #FC
        xmm = xm - (f(xm) / ff(xm))
        e = abs(xmm - xm)

        print('{} | {:.6f} | {:.6f} | {:.6f}'.format(m, xm, xmm, e))

        m += 1
        xm = xmm
        if e < erro_max:
            break

tg(lambda x : x * x - 5, lambda x : 2 * x, 3, 0.01)
