students={"Alice": 85, "Bob": 90, "Charlie": 78, "Dave": 92, "Eve": 88}

#print Topper
topper=max(students,key=students.get)
print("Topper:",topper)

#Print average score
average_score=sum(students.values())/len(students)
print("Average Score:",average_score)

#assign grades
grades={}
for name,score in students.items():
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
    grades[name]=grade

print("Grades:",grades)
