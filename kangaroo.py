def kangaroo(x1, v1, x2, v2):

    if (x1-x2)*(v1-v2) < 0:

        if (abs(x1-x2))%(abs(v2-v1)) ==0:

            return 'YES'

    return 'NO'
