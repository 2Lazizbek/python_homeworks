numbers = [-5, 8, 0, 6, 6, 19, 21, 2, 11, 19, 17, 0]
no_dup_set = set()
sorted_numbers = [number for number in numbers if number not in no_dup_set and not no_dup_set.add(number)]
print(sorted_numbers)