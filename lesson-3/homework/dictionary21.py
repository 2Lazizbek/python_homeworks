fruits = {5: 'Apple', 4: 'Banana', 3: 'Orange', 2: 'Pineapple', 1: 'Mango', 6: 'Apple'}
fruits2 = dict(sorted(fruits.items(), key=lambda x: x[1]))
print(fruits2)