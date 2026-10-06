# Exercise 6: Bank Loan Repayment Simulator
# asks for a loan, an annual interest rate, and a monthly payment,
# then pays it down month by month to see how long it takes


def get_number(prompt, allow_zero=False):
    # keeps asking until they type a real number that makes sense
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue

        if value < 0 or (value == 0 and not allow_zero):
            print("That number has to be bigger than 0.")
            continue

        return value


def simulate_repayment(loan_amount, annual_rate, monthly_payment):
    # interest rate is yearly, so split it into 12 for each month
    monthly_rate = annual_rate / 100 / 12

    balance = loan_amount
    months = 0
    total_interest = 0

    print(f"\n{'Month':<8}{'Interest':>12}{'Payment':>14}{'Balance':>16}")
    print("-" * 50)

    while balance > 0:
        interest = balance * monthly_rate
        balance += interest
        total_interest += interest

        # last month you only pay what's left, not the full payment
        payment = min(monthly_payment, balance)
        balance -= payment
        months += 1

        interest_text = f"${interest:,.2f}"
        payment_text = f"${payment:,.2f}"
        balance_text = f"${balance:,.2f}"
        print(f"{months:<8}{interest_text:>12}{payment_text:>14}{balance_text:>16}")

    return months, total_interest


def main():
    loan_amount = get_number("Loan amount: $")
    annual_rate = get_number("Annual interest rate (%, e.g. 6 for 6%): ", allow_zero=True)
    monthly_payment = get_number("Monthly payment: $")

    # if the payment doesn't even cover the first month's interest, the
    # balance grows forever and the loop would never end
    first_month_interest = loan_amount * annual_rate / 100 / 12
    if monthly_payment <= first_month_interest:
        print(f"\nThat payment won't work. The first month's interest alone is ${first_month_interest:,.2f},")
        print("so the loan would never get paid off. Try a bigger payment.")
        return

    months, total_interest = simulate_repayment(loan_amount, annual_rate, monthly_payment)

    years = months // 12
    leftover_months = months % 12

    print("-" * 50)
    print(f"Paid off in {months} months ({years} yr, {leftover_months} mo)")
    print(f"Total interest paid: ${total_interest:,.2f}")
    print(f"Total paid:          ${loan_amount + total_interest:,.2f}")


main()