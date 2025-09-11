income = float(input("Input your gross income (per week): "))
expenses = float(input("Input your expenses (per week): "))
total_income = income - expenses
print("Your total monthly income after expenses is: ", total_income)

from Calculator import calc

calc.doOperation()