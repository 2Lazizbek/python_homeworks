robert = {
    'math': 90,
    'physics': 86,
    'literature': 72
}
key = "math"
if key in robert:
    robert.pop(key)
    print(robert)
else:
    print("key does not exist")