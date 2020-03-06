if __name__ == '__main__':
    N = int(input())
    mylist=[]

    for _ in range(N):
        action, *args=input().split()
        args=list(map(int, args))
        if action == 'print':
            eval(action)(mylist)
        else:
            action = 'list.' + action
            eval(action)(mylist, *args)
