import tkinter as tk

def calculate_profit():
    initial_capital = float(initial_capital_entry.get())
    annual_interest_rate = float(annual_interest_rate_entry.get())
    model_duration = int(model_duration_entry.get())

    profit = []
    for year in range(1, model_duration + 1):
        yearly_profit = initial_capital * (annual_interest_rate / 100)
        profit.append(yearly_profit)
        initial_capital += yearly_profit

    result_label.config(text=f"Total profit for {model_duration} years: ${sum(profit):.2f}")

# Create the main window
root = tk.Tk()
root.title("Financial Model")

# Create and arrange elements on the window
tk.Label(root, text="Initial Capital:").grid(row=0, column=0)
initial_capital_entry = tk.Entry(root)
initial_capital_entry.grid(row=0, column=1)

tk.Label(root, text="Annual Interest Rate (%):").grid(row=1, column=0)
annual_interest_rate_entry = tk.Entry(root)
annual_interest_rate_entry.grid(row=1, column=1)

tk.Label(root, text="Model Duration (years):").grid(row=2, column=0)
model_duration_entry = tk.Entry(root)
model_duration_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate Profit", command=calculate_profit)
calculate_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

# Run the main program loop
root.mainloop()