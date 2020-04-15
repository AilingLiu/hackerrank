def is_late(d1, m1, y1, d2, m2, y2):

    if y2 > y1: #2001 > 2000, not late
        return False
    elif y2 == y1: #2000 == 2000, same year, continue
        if m2 > m1: # Feb > Jan, not late
            return False
        elif m2 == m1: # Feb = Feb, same month, continue
            if d2 >= d1: # 13 >= 13, not late
                return False
    return True # otherwise

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):

    if is_late(d1, m1, y1, d2, m2, y2):

        if y1 > y2:
            return 10000
        elif m1 > m2:
            return 500 * (m1-m2)
        else:
            return 15*(d1-d2)
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
