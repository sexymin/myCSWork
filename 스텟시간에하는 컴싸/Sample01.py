sample01 = [4,77,8,2,9,11,66]
sample02 = [66,55,4,3,2,5,21,85,22]
sample03 = [5,6,7,8,33,33,33,33,22,22,11,11,11,11,1,2,3,66,77,23]

from statistics import mean, mode, median

# return mean
def findMean(givenList : list) -> int:
    return mean(givenList)

# return mode 
def findMode(givenList : list) -> int:
    return mode(givenList)

# return median
def findMedian(givenList : list) -> int:
    return median(givenList)

# return range
def findRange(givenList : list) -> int:
    return max(givenList) - min(givenList)


print("Sample01:")
print("Mean:", findMean(sample01))
print("Mode:", findMode(sample01))
print("Median:", findMedian(sample01))
print("Range:", findRange(sample01))

print("Sample02:")
print("Mean:", findMean(sample02))
print("Mode:", findMode(sample02))
print("Median:", findMedian(sample02))
print("Range:", findRange(sample02))

print("Sample03:")
print("Mean:", findMean(sample03))
print("Mode:", findMode(sample03))
print("Median:", findMedian(sample03))
print("Range:", findRange(sample03))