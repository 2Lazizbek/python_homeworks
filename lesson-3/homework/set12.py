numbers = {1, 2, 3, 4}
element = 2
if element not in numbers:    
    numbers.add(element)
    print(numbers)
else:
    print('Element already exists in the set')