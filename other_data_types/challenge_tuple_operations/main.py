# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = shelf.count ("apples")
banana_index =shelf.index ("bananas")
grapes_count = shelf.count ("grapes")
oranges_index = shelf.index ("oranges")

if apple_count < 5:
    print ("Apples need to be restocked.")
else: 
    print ("Apples are sufficiently stocked")

if grapes_count == 1:
    print ("Grapes need to be restocked.")
else:
    print ("Grapes are sufficiently stocked")

if "oranges" not in shelf:
    print ("Oranges are out of stock.")
else:
    print("Oranges are at index:", + (oranges_index))


print("Number of Apples:", apple_count)
print("First Banana Index:", banana_index)

