txt = "abcabcdabcdeabcdefabcdefgabcdefghabcdefghiabcdefghijabcdefghijkabcdefghijkla"
i = 0
used  = set()
while i+3 < len(txt)-1:
    print(txt[i:i+3], end="")
    i += 3
    while txt[i-1] in "aeiouyAEIOUY" or txt[i-1] in used:
        print(txt[i], end="")
        i += 1
    if i < len(txt)-1:
        print("_", end="")
        used.add(txt[i-1])
    else:
        break
else:
    print(txt[i:])