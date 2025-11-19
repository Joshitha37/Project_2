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

    def save_expenses_to_file(self):
        file = open("expenses.txt", "w")   # open file for writing

        for cat in self.categories:
            file.write(cat.expense_type + "\n")

            for i in range(len(cat.categories)):
                item = cat.categories[i]
                cost = cat.expenses[i]
                file.write(item + " " + str(cost) + "\n")

            file.write("\n")

        file.close() 
        messagebox.showinfo("Saved", "Expenses have been saved to expenses.txt.")
    
    def load_expenses_from_file(self):
        try:
            file = open("expenses.txt", "r")  
            data = file.read()                
            file.close()

            messagebox.showinfo("Saved Expenses", data)

        except:
            messagebox.showerror("Error", "No saved file found.")

