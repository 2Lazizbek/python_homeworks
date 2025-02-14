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
allwords = paragraph.split()
wordlist = Counter(allwords)
wordlist = wordlist.most_common(5)
with open("word_count_report.txt", "w") as file:
    print("Total words:", len(allwords))
    file.write("Total words:" + str(len(allwords))+"\n")
    print("Top 5 common words:")
    file.write("Top 5 common words:\n")
    for key, value in wordlist:
        print(f'{key} - {value} times')
        file.write(f'{key} - {value} times\n')