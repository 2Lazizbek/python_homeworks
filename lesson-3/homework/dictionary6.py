color_white = {
    'red': 255,
    'green': 255,
    'blue': 255
}

robert = {
    'math': 90,
    'physics': 86,
    'literature': 72
}
robert_white = {**robert, **color_white}
print(robert_white)