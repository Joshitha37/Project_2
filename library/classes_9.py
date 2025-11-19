class Budget:
    def __init__(self, expense_type, example):
        self.expense_type = expense_type
        self.expenses = []
        self.categories = []
        self.example = example
    
    def add_expenses(self):
        while True:
            try:
                num_expenses = int(input(f"How many number of {self.expense_type} expenses you want to enter?: "))
                break
            except:
                print(" ** Wrong Input **. \n Please enter integers only!")

        print(f"Enter {self.expense_type} expenses in type \"cost format\". For e.g., {self.example} 10")
        for i in range(num_expenses):
            while True:
                try:
                    type, e = input(f"Enter expense {i+1} ").split()
                    self.categories.append(type)
                    self.expenses.append(float(e))
                    break
                except:
                    print()
                    print(" ## ERROR ##")
                    print(" Enter \"type cost\" format. for e.g., Milk 10")
                    print()

    def get_expenses(self):
        print(f"Total money spent on {self.expense_type} is {sum(self.expenses)}.")
        return sum(self.expenses)
    
    def write_to_file(self):
        with open("budget_data.txt", "a") as file:
            file.write(f"Category: {self.expense_type}\n")
            for item, cost in zip(self.categories, self.expenses):
                file.write(f"{item}: ${cost}\n")
            file.write("\n")  # space for readability


    def read_from_file(self):
        try:
            with open("budget_data.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No saved data found yet.")
