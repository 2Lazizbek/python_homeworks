import random
num = 8
rangestart = 1
rangeend = 99
numbers = set(random.sample(range(rangestart, rangeend + 1), num))
print(numbers)