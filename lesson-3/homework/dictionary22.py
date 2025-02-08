fruits = {5: 'Apple', 4: 'Banana', 3: 'Orange', 2: 'Pineapple', 1: 'Mango', 6: 'Apple'}
fruits2 = {key : value for key, value in fruits.items() if len(value) > 5}
print(fruits2)