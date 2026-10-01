failed_attempts = 0
deliveries_processed = 0

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            total = int(lines[0].strip())
            history = []
            for line in lines[1:]:
                if line.strip()!="":
                    history.append(int(line.strip()))

            return total, history

    except FileNotFoundError:
        return 0, []

def save_inventory(total, history):
    with open("inventory.txt", "w") as file:
        file.write(str(total) + "\n")

        for transaction in history:
            file.write(str(transaction) + "\n")

def get_valid_input():
    global failed_attempts

    value = input("Enter stock quantity (or type 'quit' to finish): ")

    if value.lower() == "quit":
        return "quit"

    if not value.isdigit():
        print("Error: Please enter a valid integer.")
        failed_attempts += 1
        return None

    return int(value)

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("\n---- Inventory Report ----")
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

inventory = 0

while True:

    delivery = get_valid_input()

    if delivery == "quit":
        break

    if delivery is None:
        continue

    inventory = process_delivery(inventory, delivery)

    tax = calculate_tax(delivery)

    deliveries_processed += 1

    print("Delivery processed:", delivery)
    print("Tax for this delivery:", tax)
    print("Current inventory:", inventory)

generate_report(inventory, failed_attempts)