fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'apple')
element = 'apple'
print([i for i, fruit in enumerate(fruits) if fruit == element])