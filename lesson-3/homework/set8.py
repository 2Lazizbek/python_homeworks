fruits = {'apple', 'banana', 'cherry'}
element = 'apple'
if element in fruits:
    fruits.remove(element)
    print(fruits)
else:
    print(f'{element} not in set')