grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50),
}
print(grocery_inventory)
print("Price of Eggs:", grocery_inventory["Eggs"][1])

price_of_Eggs = grocery_inventory["Eggs"][1]

if price_of_Eggs >=5:
    print("Eggs are too expensive, reducing the price by $1.")
    New_price_of_Eggs = price_of_Eggs -1
    print("New price:", New_price_of_Eggs)
    grocery_inventory["Eggs"] = ("Dairy", New_price_of_Eggs,30)    
else :
    ("Eggs are not expensive")
print(grocery_inventory)

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

print("Stock of Milk:", grocery_inventory["Milk"][2]) 
stock_of_milk = grocery_inventory["Milk"][2]

if stock_of_milk <=10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    stock_of_milk +=20
    grocery_inventory["Milk"] = ("Dairy", grocery_inventory["Milk"][2], stock_of_milk)
else :
    ("Milk has sufficient stock")

print("Price of Apple:", grocery_inventory["Apples"][1])
price_of_apple = grocery_inventory["Apples"][1]

if price_of_apple > 2:
    print("Remove Apple")  

print("Updated inventory:", grocery_inventory)


