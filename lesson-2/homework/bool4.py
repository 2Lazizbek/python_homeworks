a, b, c = map(int, input("Enter 3 numbers seperated by space: ").split())
if a not in [b,c]:
    print("All 3 numbers are different.")
else:
    print("All 3 numbers are not different.")