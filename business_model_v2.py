import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_growth():
    initial_capital = float(initial_capital_entry.get())
    annual_interest_rate = float(annual_interest_rate_entry.get()) / 100
    model_duration = int(model_duration_entry.get())
    monthly_contributions = float(monthly_contributions_entry.get())
    inflation_rate = float(inflation_rate_entry.get()) / 100

    years = list(range(model_duration + 1))
    growth = []
    inflation_adjusted_growth = []
    capital_curve = []

    for year in years:
        if year == 0:
            investment = initial_capital
        else:
            investment = (investment + monthly_contributions * 12) * (1 + annual_interest_rate)
        growth.append(investment)
        inflation_adjusted_growth.append(investment / ((1 + inflation_rate) ** year))
        capital_curve.append(investment - (monthly_contributions * 12 * year))

    plot_growth(years, growth, inflation_adjusted_growth, capital_curve)

def plot_growth(years, growth, inflation_adjusted_growth, capital_curve):
    plt.figure(figsize=(8, 4))
    plt.plot(years, growth, label="Investment Growth")
    plt.plot(years, inflation_adjusted_growth, label="Inflation Adjusted Growth")
    plt.plot(years, capital_curve, label="Capital Curve")
    plt.xlabel("Years")
    plt.ylabel("Value")
    plt.title("Investment Growth and Capital Curve Over Time")
    plt.legend()

    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=6, column=0, columnspan=2)

# Create the main window
root = tk.Tk()
root.title("Enhanced Financial Model")

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

tk.Label(root, text="Monthly Contributions:").grid(row=3, column=0)
monthly_contributions_entry = tk.Entry(root)
monthly_contributions_entry.grid(row=3, column=1)

tk.Label(root, text="Inflation Rate (%):").grid(row=4, column=0)
inflation_rate_entry = tk.Entry(root)
inflation_rate_entry.grid(row=4, column=1)

calculate_button = tk.Button(root, text="Calculate Growth", command=calculate_growth)
calculate_button.grid(row=5, columnspan=2)

# Run the main program loop
root.mainloop()