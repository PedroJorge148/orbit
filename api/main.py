import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk  # Ensure Pillow is installed

# Create the main window
root = tk.Tk()
root.title("GUI Example")
root.geometry("800x600")
root.configure(bg='black')

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Add menu items
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Main", menu=file_menu)
file_menu.add_command(label="LS")
file_menu.add_command(label="FFT")
file_menu.add_command(label="Wavelet")
file_menu.add_command(label="Diagram")

# Create a frame for the search bar and table
frame = tk.Frame(root, bg='black')
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create the search bar
search_label = tk.Label(frame, text="id", bg='black', fg='white')
search_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

search_entry = tk.Entry(frame)
search_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

search_button = tk.Button(frame, text="Search", bg='orange')
search_button.grid(row=0, column=2, padx=5, pady=5, sticky='w')

sec_label = tk.Label(frame, text="Sec", bg='black', fg='white')
sec_label.grid(row=0, column=3, padx=5, pady=5, sticky='w')

# Create a Treeview widget for the table
tree = ttk.Treeview(frame, columns=("ID", "Sector"), show='headings', height=10)
tree.heading("ID", text="ID")
tree.heading("Sector", text="Sector")

tree.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

# Add sample data
tree.insert("", "end", values=("123", "25"))

# Configure column weights
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.rowconfigure(1, weight=1)

# Create a frame for the plot
plot_frame = tk.Frame(root, bg='black')
plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create a sample plot
fig = Figure(figsize=(5, 4), dpi=100)
t = [0.1 * i for i in range(100)]
y = [i ** 2 for i in t]
plot = fig.add_subplot(111)
plot.plot(t, y)

# Embed the plot in the Tkinter GUI
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Start the main event loop
root.mainloop()
