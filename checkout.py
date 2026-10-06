# Exercise 1: Retail Checkout Simulation
# Lets a customer enter item prices one at a time (0 to finish),
# then prints the total, average item cost, and number of items.


def main():
    prices = []  # Empty list that will hold every valid price entered

    print("Enter the price of each item. Enter 0 when you're done.")

    # while True keeps looping until we hit "break" (when the user enters 0)
    while True:
        entry = input("Item price: $").strip()

        # Input validation: try to convert the entry to a number.
        # If the user types something like "abc", float() fails and
        # we ask again instead of letting the program crash.
        try:
            price = float(entry)
        except ValueError:
            print("Please enter a number (e.g., 4.99).")
            continue  # Skip the rest of this loop and ask again

        if price == 0:
            break  # 0 means the customer is done, so exit the loop
        elif price < 0:
            print("Price can't be negative. Try again.")
            continue

        prices.append(price)  # Add the valid price to the end of the list

    # After the loop: calculate the results from the list
    item_count = len(prices)  # len() counts how many items are in the list

    # If nothing was entered, skip the math (avoids dividing by zero)
    if item_count == 0:
        print("\nNo items purchased.")
    else:
        total = sum(prices)           # sum() adds up every price in the list
        average = total / item_count

        print("\n----- Checkout Summary -----")
        print(f"Items bought:      {item_count}")
        print(f"Total purchase:    ${total:,.2f}")
        print(f"Average item cost: ${average:,.2f}")


main()