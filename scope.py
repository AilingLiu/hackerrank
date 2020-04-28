class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        max_diff = 0
        for i in range(len(self.__elements)):
            for j in range(i, len(self.__elements)):
                diff = abs(self.__elements[i] - self.__elements[j])
                max_diff = max(max_diff, diff)        
        d.maximumDifference = max_diff

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
