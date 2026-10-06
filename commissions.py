# Exercise 4: Sales Commission Calculator
# figures out each employee's 10% commission and prints a leaderboard,
# highest commission first


def calculate_commission(sales_amount, rate=0.10):
    # rate defaults to 10% but could be changed if the company changes it
    return sales_amount * rate


def main():
    sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

    commissions = {}

    # run each person's sales through the function and save the result
    for employee, amount in sales.items():
        commissions[employee] = calculate_commission(amount)

    # sort names by commission, biggest first
    ranked = sorted(commissions, key=commissions.get, reverse=True)

    print("========= Commission Leaderboard =========")
    print(f"{'Rank':<6}{'Employee':<12}{'Sales':>10}{'Commission':>14}")
    print("-" * 42)

    # enumerate gives a counter alongside each name, starting at 1 for the rank
    for rank, employee in enumerate(ranked, start=1):
        sales_text = f"${sales[employee]:,.2f}"
        commission_text = f"${commissions[employee]:,.2f}"
        print(f"{rank:<6}{employee:<12}{sales_text:>10}{commission_text:>14}")


main()