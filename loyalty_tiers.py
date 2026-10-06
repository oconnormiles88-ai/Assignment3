# Exercise 8: Customer Loyalty Tiers
# puts each customer into Bronze, Silver, or Gold based on how much
# they've spent, then counts how many ended up in each tier


def get_tier(total_spent):
    if total_spent >= 5000:
        return "Gold"
    elif total_spent >= 1000:
        # using >= 1000 here instead of "<= 4999" so someone at $4,999.50
        # doesn't fall through the cracks between tiers
        return "Silver"
    else:
        return "Bronze"


def main():
    # made up customers. a few are right on the cutoffs to make sure
    # the tiers split correctly
    customers = {
        "Jordan": 450.00,
        "Priya": 1200.00,
        "Marcus": 7800.00,
        "Elena": 999.99,
        "Tyler": 3250.50,
        "Grace": 5000.00,
        "Andre": 1000.00,
        "Sofia": 4999.99,
        "Ben": 150.00,
        "Hannah": 12400.00,
    }

    # start every tier at 0 so it still shows up even if nobody's in it
    tier_counts = {"Gold": 0, "Silver": 0, "Bronze": 0}

    print("=========== Customer Tiers ===========")
    print(f"{'Customer':<12}{'Total Spent':>14}{'Tier':>10}")
    print("-" * 38)

    for name, total_spent in customers.items():
        tier = get_tier(total_spent)
        tier_counts[tier] += 1

        spent_text = f"${total_spent:,.2f}"
        print(f"{name:<12}{spent_text:>14}{tier:>10}")

    print("\n========== Tier Summary ==========")
    for tier, count in tier_counts.items():
        print(f"{tier:<10}{count:>3} customers")

    print("-" * 34)
    print(f"{'Total':<10}{len(customers):>3} customers")


main()