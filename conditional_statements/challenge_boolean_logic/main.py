seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
overstock_risk = seasonal and (current_stock > high_stock_threshold)
discount_eligible = (not selling_well) and (not on_sale)
make_discount = overstock_risk or discount_eligible

#print("Should the item be discounted?", make_discount)

account_balance = 10000
withdraw_amount = 2000
daily_limit = 5000
is_account_active = True
is_pin_correct = True
enough_balance = account_balance >= withdraw_amount
within_daily_limit = withdraw_amount <= daily_limit
security_check = is_account_active and is_pin_correct
allow_withdrawal = enough_balance and within_daily_limit and security_check

print("Can the withdrawal be approved?", allow_withdrawal)