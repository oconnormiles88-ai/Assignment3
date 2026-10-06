# Exercise 3: Expense Report Categorizer
# adds up an employee's expenses for each category and the grand total,
# then prints it as a report


def main():
    expenses = {
        "Travel": [500, 200],
        "Meals": [40, 60, 30],
        "Supplies": [100],
    }

    grand_total = 0
    item_count = 0

    print("=========== Expense Summary Report ===========")
    print(f"{'Category':<15}{'Items':>8}{'Total':>15}")
    print("-" * 46)

    # outer loop goes through each category
    for category, amounts in expenses.items():
        category_total = 0

        # inner loop adds up every expense in that category
        for amount in amounts:
            category_total += amount

        grand_total += category_total
        item_count += len(amounts)

        # turn the total into a dollar string first so it lines up in the column
        total_text = f"${category_total:,.2f}"
        print(f"{category:<15}{len(amounts):>8}{total_text:>15}")

    print("-" * 46)
    grand_text = f"${grand_total:,.2f}"
    print(f"{'Grand Total':<15}{item_count:>8}{grand_text:>15}")


main()