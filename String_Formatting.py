def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])

    for i in range(1, n+1):
        a = int(i)
        o = oct(a)[2:]
        h = hex(a)[2:].upper()
        b = bin(a)[2:]
        result = [str(a), o, h, b]
        forms = [x.rjust(width) for x in result]
        print(*forms)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
