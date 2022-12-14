from math import *

def j(a, b, x0, e_max):
    s = 0
    ci = x0
    it = 1
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i != j:
                a[i][j] = (a[i][j] / a[i][i]) * -1
        b[i] /= a[i][i]
        a[i][i] = 0
    show(a)

    #Cal' convergence:
    for i in range(len(a)):
        for j in range(len(a[i])):
            s += a[i][j] ** 2
    print('||G|| = {}'.format(sqrt(s)))

    #Table
    while True:
        tarr = []
        for i in range(len(a)):
            v = 0
            for j in range(len(a[i])):
                v += a[i][j] * ci[j]
            v += b[i]
            tarr.append(v)

        e_values = 0
        for i in range(len(tarr)):
            e_values += (tarr[i] - ci[i]) ** 2
        e = sqrt(e_values)

        print('\n', it)
        print_arr(tarr)
        print('error = {:.5f}'.format(e))

        it += 1
        ci = tarr

        if (e < e_max):
            break

def show(a):
    print('---------------------------------')
    for i in range(len(a)):
        for j in range(len(a[i])):
            print('{:.5f}'.format(a[i][j]), end = ' ')
        print()
    print('---------------------------------')

def print_arr(a):
    print('---------------------------------')
    print('[', end = '')
    for i in range(len(a)):
        print('{:.5f}'.format(a[i]), end = ', ')
    print(']')

