a, b, c = map(int, input("Enter 3 numbers seperated by space: ").split())
if a != b and a != c and c != b:
    print("All 3 numbers are different.")
else:
    print("All 3 numbers are not different.")