PRICES = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 330}
print("Available:", ", ".join(PRICES))

lines, total = [], 0
while True:
    name = input("Stock name (or 'done'): ").upper().strip()
    if name == "DONE":
        break
    if name not in PRICES:
        print("Unknown stock, try again.")
        continue
    qty = input("Quantity: ")
    if not qty.isdigit():
        print("Enter a whole number.")
        continue
    value = PRICES[name] * int(qty)
    total += value
    lines.append(f"{name} x {qty} @ ${PRICES[name]} = ${value}")

print("\n".join(lines))
print(f"Total investment: ${total}")
with open("portfolio.txt", "w") as f:
    f.write("\n".join(lines) + f"\nTotal: ${total}\n")
