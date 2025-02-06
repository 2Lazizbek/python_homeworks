text = input("Input string: ")
# for char in "aioeuyAIOUEY":
#     text = text.replace(char, "*")
# print(text)

print(''.join([char if char not in "aioeuyAIOUEY" else '*' for char in text]))