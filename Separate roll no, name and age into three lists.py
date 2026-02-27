# List of tuples (roll_no, name, age)
students = [
    (1, "Rahul", 20),
    (2, "Priya", 19),
    (3, "Amit", 21)
]

roll_list = []
name_list = []
age_list = []

for student in students:
    roll_list.append(student[0])
    name_list.append(student[1])
    age_list.append(student[2])

print("Roll Numbers:", roll_list)
print("Names:", name_list)
print("Ages:", age_list)