# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


if __name__ == '__main__':
    n, m = map(int, input().split())

    d = defaultdict(list)

    for i in range(n):
        d[input()].append(i+1) 
    
    for i in range(m):
        l = d[input()]
        if l:
            print(*l)
        else:
            print(-1)
