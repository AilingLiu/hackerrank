def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    size = int(n/k)

    for i in range(size):
        word = ''
        for letter in string[(i*k):(i+1)*k]:
            if letter not in word:
                word+=letter
        print(word)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
