import tkinter as tk
from dict_methods import add_item, sort_entries

cart = {}
root = tk.Tk()
root.title("Shopping Cart")
root.configure(bg="#f5f5f5", padx=20, pady=20)

ITEMS = ["Apple", "Banana", "Carrot", "Corn", "Tomato", "Grapes"]

item_frame = tk.LabelFrame(root, text="Items", padx=10, pady=10, bg="#f5f5f5")
item_frame.grid(row=0, column=0, sticky="n", padx=(0, 15))

tk.Label(item_frame, text="Image", width=10, bg="#f5f5f5", font=("Arial", 9, "bold")).grid(row=0, column=0)
tk.Label(item_frame, text="Item", width=10, bg="#f5f5f5", font=("Arial", 9, "bold")).grid(row=0, column=1)
tk.Label(item_frame, text="Qty", width=6, bg="#f5f5f5", font=("Arial", 9, "bold")).grid(row=0, column=2)
tk.Label(item_frame, text="", width=8, bg="#f5f5f5").grid(row=0, column=3)

#Store for entries and image
entries = {}
image_labels = {}

for i, item_name in enumerate(ITEMS, start=1):
    img = tk.PhotoImage(file=f"images/{item_name.lower()}.png")
    img_lbl = tk.Label(item_frame, image=img, width=60, height=60,
                       relief="groove", bg="#ffffff")
    img_lbl.image = img
    img_lbl.grid(row=i, column=0, padx=4, pady=4)
    image_labels[item_name] = img_lbl

    tk.Label(item_frame, text=item_name, width=10, anchor="w",
             bg="#f5f5f5", font=("Arial", 10)).grid(row=i, column=1, padx=4)

    entry = tk.Entry(item_frame, width=6, justify="center")
    entry.insert(0, "1")
    entry.grid(row=i, column=2, padx=4, pady=4)
    entries[item_name] = entry

    add_btn = tk.Button(
        item_frame, text="Add",
        command=lambda name=item_name: add_single(name),
        width=6
    )
    add_btn.grid(row=i, column=3, padx=4, pady=4)

cart_frame = tk.LabelFrame(root, text="Your Cart", padx=10, pady=10, bg="#f5f5f5")

cart_frame.grid(row=0, column=1, sticky="n")

cart_display = tk.Text(cart_frame, width=30, height=18, state="disabled",
                       font=("Courier", 10), bg="#ffffff")
cart_display.pack()

total_label = tk.Label(cart_frame, text="Total items: 0",
                       font=("Arial", 10, "bold"), bg="#f5f5f5")
total_label.pack(pady=(8, 4))


btn_frame = tk.Frame(cart_frame, bg="#f5f5f5")

btn_frame.pack(pady=(4, 0))



def refresh_cart_display():
    """Redraw the cart contents and total in the Text widget."""
    cart_display.configure(state="normal")
    cart_display.delete("1.0", tk.END)

    if not cart:
        cart_display.insert(tk.END, "(empty)")
    else:
        for item_name, qty in cart.items():
            cart_display.insert(tk.END, f"  {item_name:<12} x{qty}\n")

    cart_display.configure(state="disabled")
    total_label.configure(text=f"Total items: {sum(cart.values())}")


def add_single(name):
    """Read qty from the entry for *name* and add to cart via dict_methods."""
    global cart
    try:
        qty = int(entries[name].get())
        if qty < 1:
            raise ValueError
    except ValueError:
        qty = 1
        entries[name].delete(0, tk.END)
        entries[name].insert(0, "1")

    cart = add_item(cart, [name] * qty)
    refresh_cart_display()


def add_all():
    """Add every item whose qty entry is >= 1."""
    for name in ITEMS:
        try:
            qty = int(entries[name].get())
            if qty >= 1:
                add_single(name)
        except ValueError:
            pass


def sort_cart():
    """Sort cart alphabetically via dict_methods and refresh."""
    global cart
    cart = sort_entries(cart)
    refresh_cart_display()


def clear_cart():
    """Empty the cart."""
    global cart
    cart = {}
    refresh_cart_display()


#cart actions
tk.Button(btn_frame, text="Add All", command=add_all,
          width=8).grid(row=0, column=0, padx=4)
tk.Button(btn_frame, text="Sort A-Z", command=sort_cart,
          width=8).grid(row=0, column=1, padx=4)
tk.Button(btn_frame, text="Clear", command=clear_cart,
          width=8).grid(row=0, column=2, padx=4)

refresh_cart_display()
root.mainloop()