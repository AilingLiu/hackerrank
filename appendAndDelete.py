from collections import Counter

def appendAndDelete(s, t, k):
    scn = Counter(s)
    tcn = Counter(t)

    to_delete = 0
    to_append = 0

    for key, val in scn.items():
        if tcn[key]:
            if tcn[key] > val:
                to_append += (tcn[key]-val)
            else:
                to_delete += (val - tcn[key])
        else:
            to_delete += val

    return to_delete, to_append

if __name__ == '__main__':
    s = 'hackerhappy'
    t = 'hackerrank'
    k = 9

    an1, an2 = appendAndDelete(s, t, k)

    print(an1)
    print(an2)
