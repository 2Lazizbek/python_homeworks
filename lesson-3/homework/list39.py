numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublistsize = 5
numbers2 = [numbers[i:i+sublistsize] for i in range(0, len(numbers), sublistsize)]
print(numbers2)