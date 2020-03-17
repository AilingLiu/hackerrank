def print_rangoli(size):
    # your code goes here
    longest = [chr(a) for a in range(96+size, 96, -1)]
    width = 4*size-3

    # upper part
    for i in range(size):
        print('-'.join(longest[:i]+list(longest[i])+longest[:i][::-1]).center(width, '-'))

    # lower part

    for i in range(size-2, -1, -1):
        print('-'.join(longest[:i]+list(longest[i])+longest[:i][::-1]).center(width, '-'))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
