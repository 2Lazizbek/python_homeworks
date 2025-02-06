text = input("Enter text: ")
vowels = 0
consonants = 0
for i in range(len(text)):
    if text[i] in "aeiouAEIOU":
        vowels += 1
    elif text[i] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consonants += 1
print("Vowels -",vowels)
print("Consonants -", consonants)