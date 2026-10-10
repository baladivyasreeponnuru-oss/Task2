# Stock Portfolio Tracker

# 1. Hardcoded dictionary of stock prices (stock name -> price per share)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

# 2. Dictionary to store what the user owns (stock name -> quantity)
portfolio = {}

print("=== STOCK PORTFOLIO TRACKER ===")
print("Available stocks:", ", ".join(stock_prices))
print("Type 'done' when you have finished adding stocks.\n")

# 3. Keep asking the user for stocks until they type 'done'
while True:
    name = input("Enter stock name: ").upper().strip()

    if name == "DONE":
        break

    if name not in stock_prices:
        print("Sorry, that stock is not available. Try again.\n")
        continue

    # Ask for quantity and make sure it is a valid whole number
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a whole number.\n")
        continue

    if quantity <= 0:
        print("Quantity must be greater than 0.\n")
        continue

    # If the stock is already in the portfolio, add to it; otherwise create it
    if name in portfolio:
        portfolio[name] += quantity
    else:
        portfolio[name] = quantity

    print(f"Added {quantity} share(s) of {name}.\n")

# 4. Calculate and display the results
total_investment = 0

print("\n=== YOUR PORTFOLIO ===")
if len(portfolio) == 0:
    print("You did not add any stocks.")
else:
    for name, quantity in portfolio.items():
        price = stock_prices[name]
        value = price * quantity
        total_investment += value
        print(f"{name}: {quantity} x ${price} = ${value}")

    print("----------------------")
    print(f"Total investment: ${total_investment}")

    # 5. Optionally save the result to a text file
    save = input("\nSave result to a file? (y/n): ").lower().strip()
    if save == "y":
        with open("portfolio.txt", "w") as file:
            file.write("STOCK PORTFOLIO\n")
            file.write("---------------\n")
            for name, quantity in portfolio.items():
                price = stock_prices[name]
                file.write(f"{name}: {quantity} x ${price} = ${price * quantity}\n")
            file.write("---------------\n")
            file.write(f"Total investment: ${total_investment}\n")
        print("Saved to portfolio.txt")