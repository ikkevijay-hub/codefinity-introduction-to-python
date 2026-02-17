grocery_items = "milk cheese bread apples oranges chicken"


name = "Rahul"
age = 25
print(f"Hello, {name}! You are {age} old." )

customer = "Anita"
balance = 15000.75
print(f"{customer}, your current balance is {balance} ")

student = "Riya"
marks = 88
print(f"Student {student} scored {marks} marks in the exam")

username = "ViPu75"
password = "Rul#03!18"
print(f"{username} | {password}")

item = "Eggs"
quantity = 12
price_per_item = 5.5
total_price = quantity * price_per_item
print(f"{quantity} {item} at {price_per_item} each cost $ {total_price} in total")

  
customer_name = "Rahul"
account_balance = 15000
transaction_amount = 2500
transaction_type = "withdrawal" 
transaction_successful = True
currency = "INR"
low_balance_warning = " "

if transaction_type == "withdrawal"and transaction_successful:
    account_balance -= transaction_amount
    status = "successful"
elif transaction_type1 == "deposit" and transaction_successful:
    account_balance += transaction_amount  
    status = "successful"
else : 
    status = "failed"

if account_balance < 5000:
    low_balance_warning = "Warning: Low Balance!"

print(f"""
Transaction Alert:
Customer: {customer_name}
Transaction: {transaction_type.capitalize()} of {transaction_amount} {currency}
Status: {status}
Remaining Balance: {account_balance} {currency}
{low_balance_warning}
""")