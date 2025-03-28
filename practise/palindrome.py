def palindrome(text) -> bool:
    if len(text) == 0 or len:
        return True
    if text[0] == text[-1]:
        return palindrome(text[1:-1])
    else:
        return False
word = input("Input: ")
print(palindrome(word))