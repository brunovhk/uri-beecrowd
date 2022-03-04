"""
The company ABC decided to give a salary increase to its employees, according to the following table:


Salary	Readjustment Rate
0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Above 2000.00

15%
12%
10%
7%
4%


Read the employee's salary, calculate and print the new employee's salary, as well the money earned and the increase percentual obtained by the employee, with corresponding messages in Portuguese, as the below example.
Input
The input contains only a floating-point number, with 2 digits after the decimal point.

Output
Print 3 messages followed by the corresponding numbers (see example) informing the new salary, the among of money earned and the percentual obtained by the employee. Note:
Novo salario:  means "New Salary"
Reajuste ganho: means "Money earned"
Em percentual: means "In percentage"


"""

salary = float(input())

if salary <= 400.00:
    newSalary = salary + salary * 0.15
elif salary <= 800.00:
    newSalary = salary + salary * 0.12
elif salary <= 1200.00:
    newSalary = salary + salary * 0.10
elif salary <= 2000.00:
    newSalary = salary + salary * 0.07
elif salary > 2000.00:
    newSalary = salary + salary * 0.04

moneyEarned = newSalary - salary
percent = (moneyEarned / salary) * 100

print(f'Novo salario: {newSalary:.2f}\nReajuste ganho: {moneyEarned:.2f}\nEm percentual: {percent:.0f} %')
