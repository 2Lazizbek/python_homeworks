text= input("Enter text: ")

if any(char.isdigit() for char in text):
    print("There is a digit in text.")
else:    
    print("There isn't a digit in text.")