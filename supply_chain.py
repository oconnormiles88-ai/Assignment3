# Exercise 7: Simple Supply Chain Tracker
# goes through every warehouse and adds up how much of each product
# there is across the whole supply chain


def main():
    warehouses = [
        {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
        {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}},
    ]

    totals = {}

    print("=========== Stock by Warehouse ===========")

    # outer loop: one warehouse at a time
    for warehouse in warehouses:
        print(f"\n{warehouse['name']}")

        # inner loop: every product in that warehouse
        for product, quantity in warehouse["inventory"].items():
            print(f"  {product:<12}{quantity:>8,} units")

            # same counting idea as the survey. first time we see a
            # product start it at this quantity, after that add to it
            if product in totals:
                totals[product] += quantity
            else:
                totals[product] = quantity

    print("\n========= Total Across Supply Chain =========")
    grand_total = 0
    for product, quantity in totals.items():
        print(f"  {product:<12}{quantity:>8,} units")
        grand_total += quantity

    print("-" * 44)
    print(f"  {'all products':<12}{grand_total:>8,} units")


main()