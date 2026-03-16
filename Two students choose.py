# Subjects chosen by students
s1 = {'Math', 'Physics', 'Chemistry'}
s2 = {'Physics', 'Biology', 'Math'}

# 1. Common subjects
common_subjects = s1.intersection(s2)

# 2. Subjects taken only by first student
only_first = s1.difference(s2)

# 3. Subjects taken only by second student
only_second = s2.difference(s1)

# 4. Total unique subjects
total_unique = s1.union(s2)

# Display results
print("Common subjects:", common_subjects)
print("Subjects only first student:", only_first)
print("Subjects only second student:", only_second)
print("Total unique subjects:", total_unique)
