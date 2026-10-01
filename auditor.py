inventory = 0
failed_entries = 0

while True:
    stock = input("Enter the number of items in stock (or type 'exit' to finish): ")
    if stock.lower() == 'exit':
        break

    if not stock.isdigit():
        print("Invalid input. Please enter a valid number.")
        failed_entries += 1
        continue

    stock = int(stock)

    if stock < 0:
        print("Stock cannot be negative. Please enter a valid number.")
        failed_entries += 1
        continue

    inventory += stock
    print("Current inventory:", inventory)

    if inventory > 500:
        print("Warning: Inventory exceeds 500 items.")

print("Final inventory count:", inventory)
print("Number of failed entries:", failed_entries)

