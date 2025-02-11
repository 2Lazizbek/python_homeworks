def enrollment_stats(mylist):
    students = []
    fees = []
    for i in mylist:
        students.append(i[1])
        fees.append(i[2])
    return students, fees

def mean(mylist):
    return round(float(sum(mylist)/len(mylist)), 2)

def median(mylist):
    mylist.sort()
    if len(mylist) % 2 == 0:
        return round(float((mylist[len(mylist) // 2] + mylist[(len(mylist) // 2) - 1])/2), 2)
    else:
        return mylist[len(mylist)//2]


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

students, fees = enrollment_stats(universities)
mean_students = mean(students)
mean_fees = mean(fees)
median_students = median(students)
median_fees = median(fees)
print("*"*30)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(fees):,}")
print(f"\nStudent mean: {mean_students:,}")
print(f"Student median: {median_students:,}")
print(f"\nTuition mean: $ {mean_fees:,}")
print(f"Tuition median: $ {median_fees:,}")
print("*"*30)