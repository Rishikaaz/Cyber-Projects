import tkinter as tk
import re

def check_strength(pwd):
    if len(pwd) < 8:
        return "Too Short"
    if not re.search(r'[A-Z]', pwd) or not re.search(r'\d', pwd) or not re.search(r'[!@#]', pwd):
        return "Weak"
    return "Strong"

def evaluate():
    password = entry.get()
    result.set(check_strength(password))

root = tk.Tk()
root.title("Password Strength Checker")

entry = tk.Entry(root, show='*', width=30)
entry.pack(pady=10)

result = tk.StringVar()
tk.Button(root, text="Check", command=evaluate).pack()
tk.Label(root, textvariable=result).pack(pady=5)

root.mainloop()
