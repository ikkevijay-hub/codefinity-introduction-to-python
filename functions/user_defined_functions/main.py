# Call the function and print the result
#apples_total_cost = calculate_total_cost(1.50, 10)

items = ["Milk", "Bread", "Eggs", "Rice", "Apples", "Soap"]
prices = [30, 25, 60, 80, 45, 20]

combined_list = list(zip(items, prices))

total = 0

for item, price in combined_list:

    discounted_price = price

    if price % 2 == 0:
        discounted_price -= 2
        print(f"Even price discount applied on {item}")

    if price % 5 == 0:
        discounted_price -= 1
        print(f"Special Offer Item applied on {item}")

    print(f"{item} original price: {price}")
    print(f"{item} final price: {discounted_price}")

    total += discounted_price

print("Final Total:", total)

expensive_items = 0

for item, price in combined_list:
    if price >= 50:
        expensive_items += 1
        print(f"{item} is Expensive")
print(f"Number of expensive items: {expensive_items}")

highest_price = 0
expensive_items = " "

for item, price in combined_list:
    if price > highest_price:
        highest_price = price
        expensive_items = item        
print(f"Most Expensive Item : ", expensive_items)
print(f"Price:", highest_price)
    
discount = 0
if total > 200:
    discount = 10
    total -= discount
    print("Festive Discount Applied :", discount)

print("Final Total :", total)
        
        
    
    

    