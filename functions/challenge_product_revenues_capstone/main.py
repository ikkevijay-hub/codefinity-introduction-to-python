# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        result = prices[i] * quantities_sold[i]
        revenue.append(result)
    return revenue

revenue = calculate_revenue(prices, quantities_sold)
    
revenue_per_product = list(zip(products, revenue))

def formatted_output(revenue_per_product):
    sorted_list = sorted(revenue_per_product)
    for name, rev in sorted_list:
       print(f"{name.lower()} has total revenue of ${rev:.1f}")
formatted_output(revenue_per_product)

#print(f"{revenue_per_product} has total revenue of ${revenue}")

print("########################################################################")

client_name = "TechCorp Solutions"
estimated_hours = 40 
hourly_rate = 125.50 
is_priority = True 

total_cost = estimated_hours * hourly_rate
summary_label = client_name + " - Quote"
rush_fee = 0

if is_priority is True:
    rush_fee = total_cost + 500    
else:
    print("No rush fee Applicable")
    
print(f"Client:", summary_label)
print(f"Total Project Value: ${total_cost:.2f}")
print(f"High Value Project: ${rush_fee:.2f}")
print("########################################################################")

service_name = "Netflix"
monthly_cost = 15.99
account_limit = 4
is_auto_renew = True
can_afford = False

if monthly_cost <= 20.00:
    can_afford = True
else:
    print(f"Cannot Afford")

yearly_total = monthly_cost * 12

if is_auto_renew == True:
    monthly_cost = monthly_cost + 1.50
     
display_title = service_name + " Subscription"

print(f"Display Title:", display_title)
print(f"Updated Monthly Cost: ${monthly_cost:.2f}")
print(f"Annual Expense: ${yearly_total:.2f}")
print(f"Budget Approved:", can_afford)
print("########################################################################")

destination = "Japan"
has_visa = True
has_passport = True
age = 25
ticket_price = 800.00
banned_countries = ["Iran", "Pakistan"]
status = "Pending"

if has_passport and has_visa:
    if destination in banned_countries:
        status = "Entry Denied"
    else:
        status = "Entry Approved"
else:
    status = "Missing Documents"
  
if age <= 18 or age >= 65:
    ticket_price *=0.80
elif destination == "Japan" and age < 30:
    ticket_price *=0.90
else:
    print("No Discount")
            
if not has_passport:
            print("Missing Document")
    
print("Destination:", destination)
print(f"Entry Status: {status}")
print(f"Final Ticket Price: ${ticket_price:.2f}")
print("########################################################################")
 
travelers = [
    {"name": "Alice", "destination": "Iran", "has_passport": True, "has_visa": True, "age": 25, "price": 800},
    {"name": "Bob", "destination": "UK", "has_passport": True, "has_visa": True, "age": 40, "price": 1000},
    {"name": "Charlie", "destination": "UK", "has_passport": True, "has_visa": False, "age": 70, "price": 900},
    {"name": "David", "destination": "Japan", "has_passport": False, "has_visa": True, "age": 17, "price": 800},
    {"name": "Eve", "destination": "USA", "has_passport": True, "has_visa": True, "age": 12, "price": 1200}
]

banned_countries = ["Pakistan", "Korea"]    


for details in travelers:
    name = details["name"]
    destination = details["destination"]
    has_passport = details["has_passport"] 
    has_visa = details["has_visa"]
    age = details["age"] 
    price = details["price"]
    status = "Pending"
    
    if has_passport and has_visa:
        if destination in banned_countries:
            status = "Denied (Banned)"
        else:
            status = "Approved"
    else:
        status = "Denied (Missing Documents)"
    
    if age <= 18 or age >= 65:
        price *=0.80
    elif destination == "Japan" and age < 30:
        price *=0.90
        
    if not has_passport:
        print(f"!!! SECURITY ALERT: {name} is missing a passport !!!")
        print(f"Status: {status} | Price: N/A")
    else:
        print(f"{name}: {status}")
        print(f"Final Ticket Price: ${price:.2f}")
    
    print("-" * 30)  
    
            


    





    
