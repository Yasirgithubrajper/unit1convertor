import tkinter as tk
from tkinter import ttk

# Conversion functions
def convert_length():
    units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Inches": 39.3701,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Miles": 0.000621371
    }
    convert_units(units)

def convert_weight():
    units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1e+6,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    convert_units(units)

def convert_temperature():
    try:
        value = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value

        result_label.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Invalid input")

def convert_units(units):
    try:
        value = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit in units and to_unit in units:
            result = value * (units[to_unit] / units[from_unit])
            result_label.config(text=f"Result: {result:.2f} {to_unit}")
        else:
            result_label.config(text="Invalid units")
    except ValueError:
        result_label.config(text="Invalid input")

def update_units(event):
    category = category_var.get()
    if category == "Length":
        units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"]
    elif category == "Weight":
        units = ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"]
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]

    from_menu['menu'].delete(0, 'end')
    to_menu['menu'].delete(0, 'end')

    for unit in units:
        from_menu['menu'].add_command(label=unit, command=tk._setit(from_var, unit))
        to_menu['menu'].add_command(label=unit, command=tk._setit(to_var, unit))

    from_var.set(units[0])
    to_var.set(units[1])

# GUI setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Category selection
category_var = tk.StringVar(value="Length")
category_label = ttk.Label(root, text="Category:", background="#f0f0f0")
category_label.grid(row=0, column=0, padx=10, pady=10)
category_menu = ttk.OptionMenu(root, category_var, "Length", "Length", "Weight", "Temperature", command=update_units)
category_menu.grid(row=0, column=1, padx=10, pady=10)

# From unit
from_var = tk.StringVar()
from_label = ttk.Label(root, text="From:", background="#f0f0f0")
from_label.grid(row=1, column=0, padx=10, pady=10)
from_menu = ttk.OptionMenu(root, from_var, "")
from_menu.grid(row=1, column=1, padx=10, pady=10)

# To unit
to_var = tk.StringVar()
to_label = ttk.Label(root, text="To:", background="#f0f0f0")
to_label.grid(row=2, column=0, padx=10, pady=10)
to_menu = ttk.OptionMenu(root, to_var, "")
to_menu.grid(row=2, column=1, padx=10, pady=10)

# Entry for value
entry_label = ttk.Label(root, text="Value:", background="#f0f0f0")
entry_label.grid(row=3, column=0, padx=10, pady=10)
entry = ttk.Entry(root)
entry.grid(row=3, column=1, padx=10, pady=10)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=lambda: convert_length() if category_var.get() == "Length" else convert_weight() if category_var.get() == "Weight" else convert_temperature())
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(root, text="Result:", background="#f0f0f0")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Initialize units
update_units(None)

root.mainloop()
