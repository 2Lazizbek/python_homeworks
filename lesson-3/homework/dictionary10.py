color_white = {
    'red': 255,
    'green': 255,
    'blue': 255
}
key = 'red'
if color_white.get(key) is not None:
    print(key,":",color_white[key])
else:
    print("Key not found")