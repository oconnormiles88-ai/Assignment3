# Exercise 9: Business Growth Projection
# takes a starting revenue and a yearly growth rate and projects
# revenue out 10 years, compounding each year


def get_revenue():
    while True:
        try:
            revenue = float(input("Starting revenue: $").replace(",", ""))
        except ValueError:
            print("Please enter a number.")
            continue

        if revenue <= 0:
            print("Revenue has to be more than 0.")
            continue

        return revenue


def get_growth_rate():
    while True:
        # strip off a % in case they type "5%" instead of "5"
        entry = input("Yearly growth rate (%, e.g. 5 for 5%): ").strip().rstrip("%")
        try:
            rate = float(entry)
        except ValueError:
            print("Please enter a number.")
            continue

        # negative is fine (a shrinking business), but -100% or worse
        # would mean revenue hits 0 or goes negative
        if rate <= -100:
            print("Growth rate has to be more than -100%.")
            continue

        return rate


def main():
    revenue = get_revenue()
    growth_rate = get_growth_rate()
    years = 10
    starting_revenue = revenue

    print(f"\n{'Year':<6}{'Revenue':>18}{'Growth':>16}")
    print("-" * 40)
    start_text = f"${revenue:,.2f}"
    print(f"{0:<6}{start_text:>18}{'-':>16}")

    # each year grows off of last year's number, not the starting one
    for year in range(1, years + 1):
        growth = revenue * growth_rate / 100
        revenue += growth

        revenue_text = f"${revenue:,.2f}"
        growth_text = f"{'+' if growth >= 0 else '-'}${abs(growth):,.2f}"
        print(f"{year:<6}{revenue_text:>18}{growth_text:>16}")

    total_change = revenue - starting_revenue
    total_percent = total_change / starting_revenue * 100

    print("-" * 40)
    print(f"After {years} years revenue is ${revenue:,.2f}")
    print(f"That's {'+' if total_change >= 0 else '-'}${abs(total_change):,.2f} ({total_percent:+.1f}%) from where it started")


main()