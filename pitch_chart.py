# Exercise 10: Startup Pitch Deck Visualizer (ASCII Style)
# draws bar charts out of # signs for a made up startup's 5 year projections


def main():
    revenue = {
        "Year 1": 30000,
        "Year 2": 50000,
        "Year 3": 80000,
        "Year 4": 120000,
        "Year 5": 180000,
    }

    customers = {
        "Year 1": 200,
        "Year 2": 500,
        "Year 3": 900,
        "Year 4": 1500,
        "Year 5": 2300,
    }

    # each chart gets its own scale, otherwise revenue would need
    # 180,000 #'s and wouldn't fit on the screen
    charts = [
        {"title": "Projected Revenue by Year", "data": revenue, "per_hash": 10000, "is_money": True},
        {"title": "Projected Customers by Year", "data": customers, "per_hash": 100, "is_money": False},
    ]

    # outer loop: one chart at a time
    for chart in charts:
        scale_text = f"${chart['per_hash']:,}" if chart["is_money"] else f"{chart['per_hash']:,}"
        print(f"\n{chart['title']}  (each # = {scale_text})")
        print("-" * 45)

        # inner loop: one bar per year
        for year, value in chart["data"].items():
            bar_length = round(value / chart["per_hash"])

            # string multiplication, "#" * 3 gives "###"
            bar = "#" * bar_length

            value_text = f"${value:,}" if chart["is_money"] else f"{value:,}"
            print(f"{year}: {bar:<25} {value_text}")


main()