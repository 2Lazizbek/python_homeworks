fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
num = 3
fruits2 = tuple(fruit for fruit in fruits for i in range(num))
print(fruits2)