# Call the function and print the result
#apples_total_cost = calculate_total_cost(1.50, 10)

items = ["Milk", "Bread", "Eggs", "Rice", "Apples", "Soap"]
prices = [30, 25, 60, 80, 45, 20]

combined_list = list(zip(items, prices))
for item, price, in combined_list:
    print(f"Product: {item} : {price}")

total = 0
for item, price, in combined_list:
    total += price
print(f"Total Bill :{total}")

#if prices % 2 == 0:
 #   total += prices - 2
#else:
 #   total += prices
#print(f"Total Bill:" , total , "(Even price item discount applied)")

#if prices % 5 == 0:
 #   total /= prices - 5
#else:
 #   total /= prices
#print(f"Total Bill:" , total , "(Special Offer Item)")

#expensive_items = sum(prices for items, prices in combined_list)
#if expensive_items in combined_list:
 #   if prices in expensive_items > 50:
  #      print(f"Number of expensive items:", expensive_items)
 



