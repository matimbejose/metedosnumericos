def s(a, b, x, it):
    while True:
        for i in range(len(a)):
            d = b[i]
            for j in range(len(a)):
                if i != j:
                    d -= a[i][j] * x[j]

            x[i] = d / a[i][i]
        print_arr(x)
        it -= 1
        if it < 0:
            break

def print_arr(a):
    print('---------------------------------')
    print('[', end = '')
    for i in range(len(a)):
        print('{:.5f}'.format(a[i]), end = ', ')
    print(']')
