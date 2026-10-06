# DATA 4000 Assignment 3: Loops

Ten short Python programs for the loops unit (while loops, for loops, lists, dictionaries, and nested loops), all set up as business problems. Written and tested in VS Code with Python 3.14. Nothing to install, though portfolio.py uses Python's built-in `random` module.

To run any of them:

```
python checkout.py
```

Three of them ask you to type things in (checkout, loan_simulator, growth_projection). The other seven use data that's already written into the code, so they just run and print.

## The programs

| # | File | What it does |
|---|------|--------------|
| 1 | checkout.py | Enter item prices until you type 0. Prints the total, average item cost, and number of items. |
| 2 | survey.py | Counts 20 fake survey answers with a dictionary and prints each product's market share. |
| 3 | expenses.py | Uses a nested loop to total expenses by category plus a grand total, printed as a report. |
| 4 | commissions.py | A function calculates each employee's 10% commission, then prints a ranked leaderboard. |
| 5 | portfolio.py | Totals the value of a stock portfolio. Bonus: simulates a week of random ±5% daily price moves. |
| 6 | loan_simulator.py | Pays down a loan month by month with a while loop and prints how long it takes. |
| 7 | supply_chain.py | Loops through a list of warehouses to total each product across the supply chain. |
| 8 | loyalty_tiers.py | Sorts customers into Bronze, Silver, or Gold and counts how many are in each tier. |
| 9 | growth_projection.py | Projects revenue 10 years out at a given growth rate, year by year in a table. |
| 10 | pitch_chart.py | Draws ASCII bar charts with # for projected revenue and customers. |

## Sample runs

checkout.py
```
Item price: $4.99
Item price: $12.50
Item price: $20
Item price: $0

----- Checkout Summary -----
Items bought:      3
Total purchase:    $37.49
Average item cost: $12.50
```

loan_simulator.py ($10,000 at 6% paying $500 a month)
```
Paid off in 22 months (1 yr, 10 mo)
Total interest paid: $562.51
Total paid:          $10,562.51
```

pitch_chart.py
```
Projected Revenue by Year  (each # = $10,000)
---------------------------------------------
Year 1: ###                       $30,000
Year 2: #####                     $50,000
Year 3: ########                  $80,000
```

## Assumptions

- The survey (#2), loyalty customers (#8), and pitch chart numbers (#10) weren't given in the assignment, so I made up the data. The loyalty data includes customers right at $999.99, $1,000, $4,999.99, and $5,000 to check the tier cutoffs.
- Programs that take input re-ask if you type something that isn't a number instead of crashing.
- checkout.py: entering 0 right away prints "No items purchased" instead of dividing by zero.
- portfolio.py: the bonus week is 5 days since the stock market is only open Monday through Friday. Price changes build on the previous day. The numbers change every run because they're random.
- loan_simulator.py: the interest rate is yearly and gets split into 12 monthly charges. If the monthly payment is too small to cover the interest, the program says so instead of looping forever.
- growth_projection.py: growth is compounded yearly. You can type the rate as 5 or 5%, and negative growth works too.
- loyalty_tiers.py: Silver is anything from $1,000 up to just under $5,000, so amounts like $4,999.50 don't fall between tiers.