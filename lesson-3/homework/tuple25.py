numbers = (1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 3)
nocopy = set()
numbers2 = tuple(number for number in numbers if number not in nocopy and not nocopy.add(number))
print(numbers2)