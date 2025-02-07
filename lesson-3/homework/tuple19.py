numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
element = 5
numbers2 = numbers[:numbers.index(element)] + numbers[numbers.index(element) + 1:]
print(numbers2)