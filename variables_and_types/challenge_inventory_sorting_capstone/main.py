# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

length_of_name= items.split(", ")
print(len(length_of_name[0]))

candy1 = items[:9]
candy2 = items[11:20]
dry_goods = items[20: ]
category1 = "Candy Aisle"
category2 = "Pasta Aisle"
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print("We have", candy1, "for", bubblegum_price, "in the", category1)
print("We have", candy2, "for", chocolate_price, "in the", category1)
print("We have", dry_goods, "for", pasta_price, "in the", category2)