from math import *

def ig(f, x0, erro_max):
    m = 0
    xm = x0
    print('m | xm | xmm | erro')

    while True:
        #FC
        xmm = f(xm)
        #erro
        e = abs(xmm - xm)

        print('{} | {:.6f} | {:.6f} | {:.6f}'.format(m, xm, xmm, e))

        xm = xmm
        m += 1

        if (e < erro_max):
            break

ig(lambda x : -2.718281828**x - 1, -2, 0.1)
