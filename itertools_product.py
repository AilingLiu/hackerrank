# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
from itertools import product
xx = ' '.join(map(str, product(a, b)))
print(xx)
