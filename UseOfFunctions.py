import math
numbers = [1,3,5,6,9,11]
def Avg(numbers):
    average = sum(numbers) / len(numbers)
    return average

def sumSqDiff(numbers,average):
    ssd = 0
    for x in numbers:
        ssd += (x - average)**2
    return ssd

average = Avg(numbers)
ssd = sumSqDiff(numbers,average)
numberOfElements = len(numbers)

StandardDeviation = math.sqrt(ssd / numberOfElements)
print(StandardDeviation)

