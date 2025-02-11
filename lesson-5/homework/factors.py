def find_factors(num):
    factors = []
    for i in range(1,int(num**0.5 + 1)):
        if num % i == 0:
            factors.append(num // i)
            factors.append(i)
    return sorted(factors)
number = int(input("Input number: "))
factors1 = find_factors(number)
for i in factors1:
    print(f"{i} is a factor of {number}.") 