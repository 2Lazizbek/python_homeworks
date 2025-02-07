numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
subsize = 3
numbers2 = tuple(numbers[i: i + subsize] for i in range(0, len(numbers), subsize))
print(numbers2)