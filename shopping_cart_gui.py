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

# Create three buttons
button1 = tk.Button(root, text="Display Cart", command=read_notes)
button2 = tk.Button(root, text="Add Item", command=add_item)
button3 = tk.Button(root, text="Sort Items", command=sort_entries)
# Pack the buttons vertically
button1.pack()
button2.pack()
button3.pack()

lb = tk.Listbox(root)
lb.pack()

root.mainloop()