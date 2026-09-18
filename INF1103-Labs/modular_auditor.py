def get_valid_input():
    "Ask the user for a delivery amount and validate the input."

    while True:
        value = input("Enter the stock quantity (or type 'quit' to finish): ")
        
        if value.lower() == "quit":
            return "quit"
        
        if value.isdigit():
            return int(value)
        print("Invalid input. Please enter a valid number.")

def process_delivery(current_total, new_value):
    "Update the inventory with the new delivery amount."
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    "Calculate the tax for the given amount."
    tax_rate = 0.10
    return amount * tax_rate

def generate_report(total_units, failed_attempts):
    "Generate a summary report of the inventory process."

    print("\n--- Inventory Report ---")
    print("Final inventory count:", total_units)
    print("Number of failed entries:", failed_attempts)

inventory = 0
failed_attempts = 0
deliveries_processed = 0

while True:

    delivery = get_valid_input()
    if delivery == "quit":
        break

    inventory = process_delivery(inventory, delivery)

    tax = calculate_tax(delivery)

    deliveries_processed += 1

    print("Delivery processed:", delivery)
    print("Tax for this delivery:", tax)
    print("Current inventory:", inventory)

generate_report(inventory, failed_attempts)