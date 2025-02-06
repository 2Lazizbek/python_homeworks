text = input("Enter sentence: ")
print("There are", (1+(sum(1 for char in text if char == " "))), "words.")