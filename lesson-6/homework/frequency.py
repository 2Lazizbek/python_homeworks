import os
import re
from operator import itemgetter
from collections import Counter
filename = "sample.txt"

if os.path.exists(filename):
    with open(filename, "r") as file:
        paragraph = file.read().strip()
else:
    paragraph = ""

if not paragraph:
    while True:
        paragraph = input("Input a paragraph: ").strip()
        paragraph = re.sub(r"[^\w\s]", "", paragraph)  # Remove punctuation
        if paragraph:
            with open(filename, "w") as file:
                file.write(paragraph)
            break

paragraph = paragraph.lower()
allwords = re.findall(r'\w+', paragraph)
wordlist = Counter(allwords)
while True:
    try:
        top_num = int(input("Enter number of most common words to display: "))
        if top_num < 0:
            print("Please enter positive number.")
        else:
            break
    except Exception:
        print("Invadlid input")
wordlist = wordlist.most_common(top_num)
with open("word_count_report.txt", "w") as file:
    print("Total words:", len(allwords))
    file.write("Total words:" + str(len(allwords))+"\n")
    print(f"Top {top_num} common words:")
    file.write(f"Top {top_num} common words:\n")
    for key, value in wordlist:
        print(f'{key} - {value} times')
        file.write(f'{key} - {value} times\n')