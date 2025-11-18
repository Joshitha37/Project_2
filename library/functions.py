def calc_balance(income, expenses):
    print(f"Total expenses are {expenses}")
    balance = income - expenses
    return balance

def financial_status(bal):
    if bal > 0:
        return "You are doing good!"
    elif bal == 0:
        return "You broke even!"
    else:
        return "Warning: You are overspending!"
