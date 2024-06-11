import tkinter as tk
from tkinter import messagebox
import cmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Input Error", "Coefficient 'a' cannot be zero.")
            return

        # Calculate the discriminant
        discriminant = b**2 - 4*a*c

        # Find two solutions
        if discriminant > 0:
            root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
            result = f"Two distinct real roots: {root1.real:.2f} and {root2.real:.2f}"
        elif discriminant == 0:
            root = -b / (2 * a)
            result = f"One real root: {root:.2f}"
        else:
            root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
            result = f"Two complex roots: {root1} and {root2}"

        label_result.config(text=result)
        plot_quadratic(a, b, c)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def plot_quadratic(a, b, c):
    # Clear previous plots
    for widget in plot_frame.winfo_children():
        widget.destroy()

    # Generate x values
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, label=f'{a}x² + {b}x + {c}')
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax.set_title('Quadratic Function Plot')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()

    # Embed the plot in the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Setup the main window
root = tk.Tk()
root.title("Quadratic Equation Solver")

# Coefficient inputs
tk.Label(root, text="a:").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="b:").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="c:").grid(row=2, column=0, padx=5, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=5, pady=5)

# Solve button
btn_solve = tk.Button(root, text="Solve", command=solve_quadratic)
btn_solve.grid(row=3, column=0, columnspan=2, pady=10)

# Result display
label_result = tk.Label(root, text="", font=("Helvetica", 12))
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Frame for plotting
plot_frame = tk.Frame(root)
plot_frame.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
