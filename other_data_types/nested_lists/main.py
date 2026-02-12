vegetables = ["tomatoes", "potatoes", "onions"]

if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

vegetables.remove("onions")
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)

balances = [2000, 8000, 12000, 4000, 7100]
for balance in balances:

    if balance < 3000:
        print(balance, "→ Account Block Risk")

    elif 3000 <= balance <= 7000:
        print(balance, "→ Maintain Balance Warning")

    else:
        print(balance, "→ Healthy Account")

           

