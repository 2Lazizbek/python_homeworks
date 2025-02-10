list1 = [1, 1, 2]
list2 = [2, 3, 4]
uncommon = [i for i in list1 if i not in list2]
for i in list2:
    if i not in list1:
        uncommon.append(i)
print(uncommon)