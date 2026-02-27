gross = float(input("Enter Gross Salary: "))

allowance = 0.10 * gross
deduction = 0.03 * gross

net_salary = gross + allowance - deduction

print("Net Salary =", net_salary)
