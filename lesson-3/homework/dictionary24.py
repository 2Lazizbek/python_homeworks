fruits = (1, 'apple', 2, 'banana', 3, 'orange', 4, 'pineapple', 5, 'mango', 6, 'apple')
fruits2 = {fruits[i] : fruits[i+1] for i in range(0, len(fruits), 2)}
print(fruits2)