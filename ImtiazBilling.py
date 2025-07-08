menu = {
    "Tortilla" : 8.00,
    "Taco" : 3.00,
    "Burrito" : 7.50,
    "Samosa" : 2.00,
    "Pizza" : 12.00,
    "Burger" : 6.00
}

order = {}

print("Welcome to Imtiaz Supermarket!")
print("Enter items one by one (press Ctrl+Z to finish on Windows, Ctrl+D on Mac/Linux)")

try:
    while True: 
        item = input("Item: ").strip().title()
        if item in menu:
            if item in order:
                order[item] += 1
            else:
                order[item] = 1
        else:
            print(f"{item} not found in menu. Ignored.")

except EOFError:
    pass

print("\n ---- Final Bill ----")
total = 0.0

for item, quantity in order.items():
    unit_price = menu[item]
    item_total = unit_price + quantity
    total += item_total
    print(f"{item.upper()} x {quantity} {unit_price:.2f} = {item_total:.2f}")

print("-" * 25)
print(f"Total Due: {total:.2f}")

while True:
    try:
        paid = float(input("Enter payment amount: "))
        if paid < total:
            print("Insufficient amount. Please enter enough to cover the total.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

change = paid - total

print("\n--- Receipt ---")
print(f"Paid: {paid:.2f}")
print(f"Total: {total:.2f}")
print(f"Change: {change:.2f}")
print("Thankyou for shopping at Imtiaz Supermarket.")