import tkinter as tk
from dict_methods import add_item, read_notes, update_recipes, sort_entries, send_to_store

root = tk.Tk()
root.title("Shopping Cart")

"""
Requirements
Functionality:

Display current cart contents
Allow users to add items to the cart (calls add_item())
Display total items and sorted cart (calls sort_entries())
Simple, clean layout (MVP = minimal but functional)
NO complex features — keep it simple

"""


tk.Label(root, text="Apple").grid(row=0, column=0)
tk.Label(root, text="Banana").grid(row=1, column=0)
tk.Label(root, text="Carrot:").grid(row=2, column=0)
tk.Label(root, text="Corn:").grid(row=3, column=0)
tk.Label(root, text="Tomato:").grid(row=4, column=0)
tk.Label(root, text="Grapes:").grid(row=5, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)
entry5 = tk.Entry(root)
entry6 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)
entry6.grid(row=5, column=1)

root.mainloop()