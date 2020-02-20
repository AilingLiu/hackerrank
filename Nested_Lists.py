if __name__ == '__main__':
    students={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in students:
            students[score].append(name)
        else:
            students[score]=[name]
    
    ss = sorted(students[sorted(students)[1]])
    for su in ss:
        print(su)
