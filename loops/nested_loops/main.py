produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]
print("groceries:", groceries)

for section in groceries:
    for item in section:
        print(f"Item name:", item)

print("####################################################################################")

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
