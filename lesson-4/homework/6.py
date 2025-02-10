print(2)
for num in range(3, 101, 2):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num)