def convert_cel_to_far(cel):
    return cel * 9/5 + 32
def convert_far_to_cel(far):
    return (far - 32) * 5/9
temp_far = float(input("Input temperature in degrees Fahrenheit: "))
print(f"{temp_far}°F = {round(convert_far_to_cel(temp_far), 2):.2f}°C")
temp_cel = float(input("Input temperature in degrees Celsius: "))
print(f"{temp_cel}°F = {round(convert_cel_to_far(temp_cel), 2):.2f}°C")