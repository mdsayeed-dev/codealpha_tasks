STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def main():
    print("=== STOCK PORTFOLIO TRACKER ===")
    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nStock name aur quantity daalo. Khatam karne ke liye 'done' likho.\n")

    portfolio = {}
    total = 0

    while True:
        stock = input("Stock name: ").upper().strip()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("Ye stock list me nahi hai, dobara try karo.\n")
            continue

        try:
            qty = int(input("Quantity: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Quantity ek positive number honi chahiye.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"Added {qty} x {stock}\n")

    if not portfolio:
        print("Koi stock add nahi kiya.")
        return

    lines = ["Stock Portfolio Summary", "-" * 35]
    for stock, qty in portfolio.items():
        value = qty * STOCK_PRICES[stock]
        total += value
        lines.append(f"{stock:<6} {qty:>4} x ${STOCK_PRICES[stock]:<5} = ${value}")
    lines.append("-" * 35)
    lines.append(f"Total Investment: ${total}")

    print("\n" + "\n".join(lines))

    save = input("\nResult file me save karna hai? (y/n): ").lower().strip()
    if save == "y":
        with open("portfolio.txt", "w") as f:
            f.write("\n".join(lines))
        print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()
