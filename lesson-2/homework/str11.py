text= input("Enter text: ")

if any(char.isdigit() for char in text):
    print("There is a digit in text.")
else:    
    print("There isn't a digit in text.")

# a = 0
# for char in "0123456789":
#     if char in text:
#         print("There is a digit in text.")
#         a = 1
#         break
# if a == 0:
#     print("There isn't a digit in text.")
