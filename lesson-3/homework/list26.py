fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(fruits[len(fruits)//2] if len(fruits) % 2 == 1 else print(fruits[len(fruits)//2-1:len(fruits)//2+1]))