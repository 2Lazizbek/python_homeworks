basket = {1: 'Apple', 2: 'Banana', 3: 'Orange', 4: 'Pineapple', 5: 'Mango'}
print(any(type(i) == dict for a, i in basket.items()))