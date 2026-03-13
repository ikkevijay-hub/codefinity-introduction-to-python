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

print(f"{revenue_per_product} has total revenue of ${revenue}")






    
