sentence = input("Input sentence: ")
word1 = input("Word to replace: ")
word2 = input("Word to replace with: ")
if sentence.find(word1) == -1:
    print(f'"{word1}" is not present in this sentence')
else:
    index = sentence.find(word1)
    length = len(word1)
    print(sentence[:index] + word2 + sentence[index+length:])