import os
from library import functions
from library.classes_9 import Budget 

os.system('cls' if os.name == 'nt' else 'clear')

name = input("Enter your name: ")
os.system('cls' if os.name == 'nt' else 'clear')

print(f"Hey {name}, this is BudgetBuddy! Your personal Budgeting Assistant.\n")
income = float(input("Enter your monthly income (only numbers): "))

grocery = Budget("Grocery", "Milk")
car = Budget("car", "Gas")

grocery.add_expenses()
car.add_expenses()

total_expenses = []
total_expenses.append(grocery.get_expenses())
total_expenses.append(car.get_expenses())

bal = functions.calc_balance(income, sum(total_expenses))
functions.financial_status(bal)
