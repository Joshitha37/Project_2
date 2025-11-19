import tkinter as tk
from tkinter import messagebox
from library.classes_9 import Budget
from library import functions


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class BudgetBuddyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Buddy")
        self.root.geometry("1300x800")
        self.root.config(bg="#E2FFD9")

        bg_color = "#E2FFD9"
        self.root.config(bg=bg_color)

        self.categories = []     

        
        tk.Label(root, text="Budget Buddy", font=("Monaco", 45, "bold"), bg=bg_color).pack(pady=50)

       
        tk.Label(root, text="Your Name:", bg=bg_color).pack()
        self.name_entry = tk.Entry(root, width=25)
        self.name_entry.pack(pady=15)

        
        tk.Label(root, text="Enter Monthly Income:", bg=bg_color).pack()
        self.income_entry = tk.Entry(root, width=25)
        self.income_entry.pack(pady=15)

        
        tk.Label(root, text="Create a Budget Category:", font=("Arial", 15, "bold"), bg=bg_color).pack(pady=15)

        tk.Label(root, text="Category Name:", bg=bg_color).pack()
        self.cat_name_entry = tk.Entry(root, width=25)
        self.cat_name_entry.pack(pady=15)

        tk.Button(root, text="Add Category", command=self.add_category, width=12, height=2).pack(pady=10)

       
        self.category_box = tk.Listbox(root, width=35, height=6)
        self.category_box.pack()

        
        tk.Button(root, text="Enter Expenses for Selected Category", width=25, height=2,
                  command=self.open_expense_window).pack(pady=10)

        
        tk.Button(root, text="Show Final Summary", width=15, height=2, command=self.show_summary).pack(pady=15)

    
    def add_category(self):
        name = self.cat_name_entry.get()

        if name == "":
            messagebox.showerror("Error", "Please enter a category name.")
            return

        new_cat = Budget(name, "") 
        self.categories.append(new_cat)

        self.category_box.insert(tk.END, f"{name}")
        self.cat_name_entry.delete(0, tk.END)

   
    def open_expense_window(self):
        selected = self.category_box.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a category first.")
            return

        index = selected[0]
        category_obj = self.categories[index]

        win = tk.Toplevel()
        win.title(f"{category_obj.expense_type} Expenses")

        tk.Label(win, text=f"Add expenses for {category_obj.expense_type}").pack(pady=10)
        tk.Label(win, text="Enter type & cost (like: Milk 10)").pack()

        entry = tk.Entry(win, width=30)
        entry.pack(pady=5)

        def add_exp():
            try:
                type_name, amount = entry.get().split()
                category_obj.categories.append(type_name)
                category_obj.expenses.append(float(amount))
                entry.delete(0, tk.END)
            except:
                messagebox.showerror("Error", "Format must be: item cost")

        tk.Button(win, text="Add Expense", command=add_exp).pack(pady=5)

    
    def show_summary(self):
        try:
            income = float(self.income_entry.get())
        except:
            messagebox.showerror("Error", "Income must be a number.")
            return

        total_expenses = []
        labels = []
        summary_text = ""

        for cat in self.categories:
            total = cat.get_expenses()
            total_expenses.append(total)
            labels.append(cat.expense_type)
            summary_text += f"{cat.expense_type}: ${total:.2f}\n"

        balance = functions.calc_balance(income, sum(total_expenses))
        status = functions.financial_status(balance)

        final_msg = (
            f"Name: {self.name_entry.get()}\n\n"
            f"Total Income: ${income:.2f}\n"
            f"Total Spent: ${sum(total_expenses):.2f}\n"
            f"Remaining Balance: ${balance:.2f}\n\n"
            f"{summary_text}\n"
            f"Status: {status}"
        )

        messagebox.showinfo("Budget Summary", final_msg)

        
        self.show_pie_chart(labels, total_expenses)

    def save_expenses_to_file(self):
        file = open("expenses.txt", "w")

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
    

    
    def show_pie_chart(self, labels, values):
        if sum(values) == 0:
            messagebox.showinfo("No Data", "No expenses added yet to display a chart.")
            return

        chart_win = tk.Toplevel(self.root)
        chart_win.title("Expense Breakdown Pie Chart")
        chart_win.geometry("600x600")

        fig = Figure(figsize=(5, 5))
        ax = fig.add_subplot(111)

        ax.pie(values, labels=labels, autopct="%1.1f%%")
        ax.set_title("Expenses by Category")

        canvas = FigureCanvasTkAgg(fig, master=chart_win)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)



root = tk.Tk()
app = BudgetBuddyGUI(root)
root.mainloop()
