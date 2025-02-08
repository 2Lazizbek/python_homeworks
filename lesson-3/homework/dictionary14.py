color_white = {
    'red': 255,
    'green': 255,
    'blue': 255
}
value = 255
white = {i for i in color_white if color_white[i] == value}
print(white)