# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list(map(int, input().split()))
b = []
for i in range(int(input())):
    b.append(list(map(int, input().split())))

result=True
for l in b:
    if (l==a) or (not set(l).issubset(set(a))):
        result=False

print(result)
