# Exercise 2: Market Survey Analyzer
# made up survey of 20 customers. counts how many picked each drink
# and prints each one's share of the total


def main():
    responses = [
        "coffee", "tea", "coffee", "soda", "water",
        "coffee", "tea", "soda", "coffee", "water",
        "tea", "coffee", "soda", "coffee", "tea",
        "water", "coffee", "soda", "tea", "coffee",
    ]

    counts = {}

    # add 1 to the count for each answer
    # the first time a product shows up it's not in the dict yet, so start it at 1
    for choice in responses:
        if choice in counts:
            counts[choice] += 1
        else:
            counts[choice] = 1

    total = len(responses)

    print(f"Market Share ({total} responses)")
    print("-" * 25)

    # sort so the most popular one prints first
    for product in sorted(counts, key=counts.get, reverse=True):
        share = counts[product] / total * 100
        print(f"{product}: {share:.0f}%")


main()