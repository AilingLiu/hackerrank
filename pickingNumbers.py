def pickingNumbers(a):

    unique = sorted(set(a)) #example: set([1,2,2,3,1,2])--> [1,2,3]
    #print('unique: ', unique)

    meet_cond = [unique[i] for i in range(1, len(unique)) if abs(unique[i-1]-unique[i])<=1]
    #print('filtered: ', meet_cond)

    counts = [a.count(val) for val in meet_cond] #[2,3,1]
    #print('freq: ', counts)

    max_ind = [i for i, val in enumerate(counts) if val==max(counts)] #1
    #print('indexs: ', max_ind)

    max_counts = 0
    for ind in max_ind:
        if ind == 0:
            max_counts = max(counts[ind]+counts[ind+1], max_counts)
        elif ind == (len(counts)-1):
            max_counts = max(counts[ind]+counts[ind-1], max_counts)
        else:
            max_counts = max(counts[ind]+counts[ind+1], counts[ind]+counts[ind-1], max_counts)

    #print(max_counts)
    return max_counts

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    pickingNumbers(a)
