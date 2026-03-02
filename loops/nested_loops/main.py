produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]
print("groceries:", groceries)

for section in groceries:
    for item in section:
        print(f"Item name:", item)

print("####################################################################################")

#Range - Iterating Over Indexes - Nested Loop

print(list(range(5,15)))
print(list(range(2,22,2)))

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
for item in range(len(fruits)):
    print("Index :", item)
    print("Item:", fruits[item])

numbers = [10, 20, 30, 40, 50]
print(list(range(50,0,-10)))

print(list(range(0,20,3)))

print("####################################################################################")

numbers_table = 3

for index in range(1, 11):
    result = numbers_table * index
    print(result)
    
print("####################################################################################")

for row in range(3):        # Outer loop (rows)
    for col in range(1, 5): # Inner loop (numbers)
        print(col, end=" ")
    print()  # Move to next line

print("####################################################################################")

for row in range(1,5):        # Outer loop (rows)
    for col in range(1, row + 1): # Inner loop (numbers)
        print(col, end=" ")
    print()  # Move to next line
    
print("####################################################################################")

for row in range(4, 0, -1):        
    for col in range(1, row + 1):  
        print(row, end=" ")
    print()

print("####################################################################################")

for row in range(1, 6):        # Outer loop (rows)
    for col in range(1, row + 1): # Inner loop (numbers)
        print(" * ", end=" ")
    print()  # M

print("####################################################################################")

for row in range(6, 0, -1):        
    for col in range(1, row + 1):  
        print("*", end=" ")
    print()

print("####################################################################################")

for row in range(1, 6):
    for space in range(5 - row):
        print(" ", end="")
    for star in range(row):
        print("*", end="")
    print()

print("####################################################################################")


