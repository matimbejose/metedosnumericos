def g(a, b):
    print(a, end = ' >> \n\n')
    n = len(b)
    
    #Main loop
    for k in range(n):

        #Partial Pivoting
        if a[k][k] == 0:
            for i in range(k + 1, n):
                if (a[i][k] > a[k][k]):
                    for j in range(k, n):
                        a[k][j], a[i][j] = a[i][j], a[k][j]
                    b[k], b[i] = b[i], b[k]
                    print('Changed', a)
                    break

        #Division of pivot row
        pivot = a[k][k]
        for j in range(k, n):
            a[k][j] /= pivot
        b[k] /= pivot
        show(a)
        print(b)
        

        #Elimination Loop
        for i in range(n):
            if i == k or a[i][k] == 0: continue
            factor = a[i][k]
            for j in range(k, n):
                a[i][j] -= factor * a[k][j]
            b[i] -= factor * b[k]
            show(a)
            print(b)


def show(m):
    print('------------------------')
    for i in range(len(m)):
        for j in range(len(m[i])):
            print('{:.3f} '.format(m[i][j]), end = ' ')
        print()
    print('------------------------')

g([[5, 2, 2], [1, 6, 3], [2, 2, 7]], [9, 10, 11])
