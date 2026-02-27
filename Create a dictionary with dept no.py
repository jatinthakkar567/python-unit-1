# dept_no : (roll_no, salary)
employees = {
    101: (1, 50000),
    101: (2, 60000),
    102: (3, 45000),
    102: (4, 70000),
    103: (5, 55000)
}

dept_salary = {}

# Collect salaries department-wise
for dept, data in employees.items():
    salary = data[1]
    if dept not in dept_salary:
        dept_salary[dept] = []
    dept_salary[dept].append(salary)

# Find min and max salary
for dept in dept_salary:
    print("Department:", dept)
    print("Minimum Salary:", min(dept_salary[dept]))
    print("Maximum Salary:", max(dept_salary[dept]))
    print()
