fruits = {5: 'Apple', 4: 'Banana', 3: 'Orange', 2: 'Pineapple', 1: 'Mango', 6: 'Apple'}
fruits2 = {7: 'Apple', 8: 'Banana', 9: 'Orange', 10: 'Pineapple', 1: 'Mango', 12: 'Apple'}
print(any(key in fruits for key in fruits2))