total_cost = 25.00
discount_threshold = 20.00

discountEligible = total_cost >= discount_threshold

print("Is the purchase eligible for a discount?", discountEligible)

account_balance = 10000
withdraw_amount = 2000
is_pin_correct = True
is_account_active = True

if account_balance < withdraw_amount:
    print("Insufficient funds")
elif is_pin_correct and is_account_active:  
    print("Withdrawal Allowed")
else:
    print("Cannot Process Withdrawal")

age = 30
monthly_income = 10000
credit_score = 10
existing_loan = True

if age > 35:
    print("Age-Can Process Further")
elif monthly_income > 50000 and credit_score > 8:
    print("Monthly Income-Can Process Further")
else:
    print("Loan Application Rejected")

is_member = "Active"
purchase_amount = 2000
is_festival_season = True

if is_member:
    print("Eligible for Discount")
elif purchase_amount >= 1000:
    print("Discount Eligible")
else:
    print("Discount not Eligible")

length = 10
has_number = True
has_special_char = False
has_uppercase = True

strong_password = (length >= 10) and (has_number == True) and (has_special_char == False) and (has_uppercase == True)

if strong_password :
    print("Password Accepted")
else:
    print("Password Not Accepted")


age = 21
monthly_income = 100
credit_score = 5
existing_loan = False
is_employed = True
has_criminal_record = True
loan_amount = 50

loan_approvals_status = (age>=21) and (monthly_income>=100) and (credit_score) and (is_employed) and (not has_criminal_record) and (loan_amount <= 50) and (existing_loan)

if existing_loan is True:
    print("Loan Rejected Due to existing Loan")
else:
    print("Loan Processed Further")

if loan_approvals_status:
    print("Loan Passed")
else:
    print("Loan Rejected")


has_id_card

is_employee

access_level

biometric_verified

is_weekend

is_manager_approval

blacklisted
                                                                             