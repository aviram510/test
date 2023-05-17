import sqlite3
import csv
from statistics import median
#1.
connect= sqlite3.connect('company.db')
c = connect.cursor()

#2.
c.execute('''SELECT employees.name, employees.salary, departments.department_name 
FROM employees JOIN departments ON employees.department_id = departments.id 
WHERE departments.department_name = "Sales" AND employees.salary > 50000''')
data = c.fetchall()

#3.
salaries = [row[1] for row in data]
average_salary = sum(salaries) / len(salaries)
median_salary = median(salaries)
print(f"Average salary: {average_salary}")
print(f"Median salary: {median_salary}")

#4.
department_salaries = {}
for row in data:
    department = row[2]
    salary = row[1]
    if department in department_salaries:
        if salary > department_salaries[department]:
            department_salaries[department] = salary
    else:
        department_salaries[department] = salary

for department, highest_salary in department_salaries.items():
    print(f"Highest earner in {department}: {highest_salary}")

#5.
c.execute('''SELECT name FROM employees WHERE salary = (SELECT MAX(salary) FROM employees)''')
highest_earner = c.fetchone()[0]
print(f"Highest earner in the entire company: {highest_earner}")

#6.
with open('result.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Employee Name", "Salary", "Department Name"])
    for row in data:
        writer.writerow([row[0], row[1], row[2]])

connect.close()
