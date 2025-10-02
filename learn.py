import tkinter as tk

def click_button(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())   # backend logic
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Input field
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

# Create all buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate, bg="#2196f3", fg="white")
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click_button(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", width=22, height=2, command=clear, bg="red", fg="white")
clear_btn.grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()
a = 5
b = 10  
c = a + b
print(c)                                                                                                                                                                                                                                                                                                                  