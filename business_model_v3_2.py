import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_growth():
    initial_capital = float(initial_capital_entry.get())
    model_duration = int(model_duration_entry.get())

    years = list(range(model_duration + 1))
    annual_contributions_curve = []  # Updated variable name
    inflation_adjusted_growth = []
    capital_curve = []

    annual_interest_rates = [float(rate) / 100 for rate in annual_interest_rates_entry.get().split(",")]
    annual_contributions_list = [float(contribution) for contribution in annual_contributions_entry.get().split(",")]
    annual_inflation_rates = [float(rate) / 100 for rate in annual_inflation_rates_entry.get().split(",")]

    investment = initial_capital
    annual_contributions = 0  # Initialize annual contribution variable
    annual_inflation_rate = 0  # Initialize annual inflation rate variable

    for year in years:
        if year > 0:
            annual_interest_rate = annual_interest_rates[year - 1]

            # Update annual contribution and annual inflation rate for the current year
            annual_contributions = annual_contributions_list[year - 1]
            annual_inflation_rate = annual_inflation_rates[year - 1]

            investment = (investment + annual_contributions) * (1 + annual_interest_rate)

        annual_contributions_curve.append(annual_contributions)  # Append annual contributions
        inflation_adjusted_growth.append(investment / ((1 + annual_inflation_rate) ** year))
        capital_curve.append(investment)

    plot_growth(years, annual_contributions_curve, inflation_adjusted_growth, capital_curve)  # Update this line

def plot_growth(years, annual_contributions_curve, inflation_adjusted_growth, capital_curve):
    plt.figure(figsize=(8, 4))
    plt.plot(years, annual_contributions_curve, label="Annual Contributions")  # Updated label
    plt.plot(years, inflation_adjusted_growth, label="Inflation-Adjusted Growth")
    plt.plot(years, capital_curve, label="Capital Curve")
    plt.xlabel("Years")
    plt.ylabel("Value")
    plt.title("Annual Contributions, Inflation-Adjusted Growth, and Capital Curve Over Time")  # Updated title
    plt.legend()

    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=8, column=0, columnspan=2)

# Create the main window
root = tk.Tk()
root.title("Enhanced Financial Model")

# Create and arrange elements on the window
tk.Label(root, text="Initial Capital:").grid(row=0, column=0)
initial_capital_entry = tk.Entry(root)
initial_capital_entry.grid(row=0, column=1)

tk.Label(root, text="Model Duration (years):").grid(row=1, column=0)
model_duration_entry = tk.Entry(root)
model_duration_entry.grid(row=1, column=1)

tk.Label(root, text="Annual Interest Rates (%), separated by comma:").grid(row=2, column=0)
annual_interest_rates_entry = tk.Entry(root)
annual_interest_rates_entry.grid(row=2, column=1)

tk.Label(root, text="Annual Contributions, separated by comma:").grid(row=3, column=0)
annual_contributions_entry = tk.Entry(root)
annual_contributions_entry.grid(row=3, column=1)

tk.Label(root, text="Annual Inflation Rates (%), separated by comma:").grid(row=4, column=0)
annual_inflation_rates_entry = tk.Entry(root)
annual_inflation_rates_entry.grid(row=4, column=1)

calculate_button = tk.Button(root, text="Calculate Growth", command=calculate_growth)
calculate_button.grid(row=5, columnspan=2)

# Run the main program loop
root.mainloop()
