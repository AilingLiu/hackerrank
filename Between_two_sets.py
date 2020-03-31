def getTotalX(a, b):
    # Write your code here

    get_factors = lambda x: set([i for i in range(1, x+1) if x%i==0])
    factors_in_b = [get_factors(i) for i in b]
    common_factors = set.intersection(*factors_in_b)

    candidate = common_factors.copy()

    for val in set(common_factors):
        not_factor = any(val%i for i in a)
        if not_factor:
            candidate.remove(val)

    return len(candidate)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
