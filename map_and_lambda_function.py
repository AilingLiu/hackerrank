cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    mylist=[]
    a, b = 0, 1
    for i in range(n):
        mylist.append(a)
        a, b = b, a+b
    return mylist

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
