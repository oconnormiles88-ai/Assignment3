# Exercise 5: Stock Portfolio Tracker
# adds up what the portfolio is worth (shares x price for each stock)
# bonus: fakes a week of random price moves and shows the value each day

import random


def portfolio_value(portfolio):
    total = 0
    for ticker, info in portfolio.items():
        total += info["shares"] * info["price"]
    return total


def main():
    portfolio = {
        "AAPL": {"shares": 10, "price": 170},
        "TSLA": {"shares": 4, "price": 250},
        "AMZN": {"shares": 2, "price": 130},
    }

    print("============ Portfolio Summary ============")
    print(f"{'Stock':<8}{'Shares':>8}{'Price':>12}{'Value':>14}")
    print("-" * 42)

    # go through each stock and print what that position is worth
    for ticker, info in portfolio.items():
        value = info["shares"] * info["price"]
        price_text = f"${info['price']:,.2f}"
        value_text = f"${value:,.2f}"
        print(f"{ticker:<8}{info['shares']:>8}{price_text:>12}{value_text:>14}")

    starting_value = portfolio_value(portfolio)
    total_text = f"${starting_value:,.2f}"
    print("-" * 42)
    print(f"{'Total Value':<28}{total_text:>14}")

    # ---- Bonus: one week of random price changes ----
    # 5 days since the market's only open Monday-Friday
    days = 5
    previous_value = starting_value

    print("\n========= One Week Simulation (+/- 5%) =========")
    print(f"{'Day':<8}{'Total Value':>16}{'Daily Change':>18}")
    print("-" * 42)

    # outer loop is each day, inner loop moves every stock's price that day
    for day in range(1, days + 1):
        for ticker, info in portfolio.items():
            # random number between -5% and +5%
            change = random.uniform(-0.05, 0.05)
            info["price"] = info["price"] * (1 + change)

        new_value = portfolio_value(portfolio)
        daily_change = new_value - previous_value

        value_text = f"${new_value:,.2f}"
        # + sign shows up on gains so it's easy to tell up days from down days
        change_text = f"{'+' if daily_change >= 0 else '-'}${abs(daily_change):,.2f}"
        print(f"Day {day:<4}{value_text:>16}{change_text:>18}")

        previous_value = new_value

    week_change = previous_value - starting_value
    week_percent = week_change / starting_value * 100
    print("-" * 42)
    print(f"Week change: {'+' if week_change >= 0 else '-'}${abs(week_change):,.2f} ({week_percent:+.2f}%)")


main()