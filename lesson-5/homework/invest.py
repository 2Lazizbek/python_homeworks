def invest(amount, rate, years):
    for i in range(1,years+1):
        amount *= 1+rate
        print(f"Year {i}: $ {round(amount, 2):.2f}")
amount1 = float(input("Input the initial amount: $"))
rate1 = float(input("Input the annual rate of return as fraction[5% = 0.05]: "))
years1 = int(input("Input number of years: "))
invest(amount1, rate1, years1)