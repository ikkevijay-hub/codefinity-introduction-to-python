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


has_id_card = True
is_employee = True
access_level = True
biometric_verified = True
is_weekend = False
is_manager_approval = True
blacklisted = False

office_entry = (has_id_card) and (is_employee) and (access_level) and (biometric_verified) 
(not is_weekend) and (is_manager_approval) and (not blacklisted)

if office_entry :
    print("Entry Allowed")
else :
    print("Entry Rejected")


restaurant_open = True
delivery_boy_available = True
distance_km = 10
minimum_order_amount = 500
order_amount = 400
is_raining = True
area_serviceable = True
payment_successful = True

order_accept = (restaurant_open
                and delivery_boy_available  
                and distance_km <=10 and area_serviceable
                and order_amount >= minimum_order_amount
                and is_raining 
                and payment_successful)

if order_accept:
    print("Order Accepted")
else:
    print("Order Rejected Due to :" " ") 

a = float ("5")
b = 4.8
#print(a+b)

a = int('11', 2)
#print(a)

age = 21
monthly_income = 500000
credit_score = 10
existing_loan = False
loan_amount = 50000
interest_rate = 10
loan_tenure = 12
has_criminal_record = False
employment_years = 10
is_self_employed = True
has_collateral = True
collateral_value = 25000
emi_total = loan_amount + interest_rate / loan_tenure
reason =[]

#loan_approval = (age >= 21 
#                 and age <=60
 #                and credit_score >=7
  #               and loan_amount < monthly_income
   #              and not has_criminal_record
    #             and not is_self_employed or employment_years >=3                 
     #            and not existing_loan
      #           and loan_amount > monthly_income 
       #          or (has_collateral and collateral_value >= loan_amount)
        #         and monthly_income >= loan_amount * interest_rate * loan_tenure
         #       )
#print("Status of Loan Approval = ")

if not (age <=21 and age <=60):
    reason.append("Age not within eligible range (21-60)")
if credit_score >=11:
    reason.append ("Credit score below minimum requirement")
if loan_amount > monthly_income:
    reason.append ("loan_amount > monthly_income")
if has_criminal_record:
    reason.append("Applicant has criminal record")
if existing_loan:
    reason.append("Existing loan detected")
if not is_self_employed or employment_years <=3:
    reason.append("Self-employed but experience less than 3 years")
if loan_amount > 50000:
    if not has_collateral or collateral_value > loan_amount:
        reason.append("Insufficient collateral")
if monthly_income < emi_total:
    reason.append("Income insufficient to cover EMI")

if len(reason) ==0:
    print("Loan Approved")
else:
    print("Loan Rejected")
    print("Reasons:")
    for r in reason:
        print("-", r)


age = 67
heart_rate = 130              # bpm
blood_pressure_systolic = 85  # mmHg
oxygen_level = 88             # %
temperature = 39.5            # Celsius
is_unconscious = False
has_chest_pain = True
has_severe_bleeding = False
accident_case = True
pregnant = False
chronic_disease = True
pain_scale = 9                # 1 to 10
arrival_mode = "ambulance"    # walk-in / ambulance

reason=[]

stable_condition = ("Patient is a Senior Citizen" + "Normal Blood Pressure" + "High Fever" + "Patient is Conscious" + "Mild Pain")
urgent_Condition = ("Patient is a Senior Citizen" + "Critical Patient Heart Rate more then 100 BPM" + "Elevated Blood Pressure" + "Low Oxygen Level" + "Has Chest Pain" + "Patient is Pregnant"
"Patient has Chronic Disease" + "Moderate Pain")
critical_condition = ("Patient is a Senior Citizen" + "1 Hypertension Blood Pressure" + "Patient has Severe Bleeding" + "Accident Case" + "Severe Pain" + "Patient came in Ambulance")

if not age <= 60:
    reason.append("Patient is a Senior Citizen")
if heart_rate >= 100:
    reason.append("Critical Patient Heart Rate more then 100 BPM")
if blood_pressure_systolic <= 120:
    severity = "Normal"
    reason.append("Normal Blood Pressure")
if 120 <= blood_pressure_systolic <=129:
    severity="Elevated"
    reason.append("Elevated Blood Pressure")
elif 130 <= blood_pressure_systolic <= 139:
    severity = "1 Hypertension"
    reason.append("1 Hypertension Blood Pressure")
else:
    severity = "Invalid Input"
if oxygen_level < 90:
    reason.append("Low Oxygen Level")
if temperature >=39.5:
    reason.append("High Fever")
if is_unconscious:
    reason.append("Patient is Conscious")
if has_chest_pain:
    reason.append("Has Chest Pain")
if has_severe_bleeding:
    reason.append("Patient has Severe Bleeding")
if accident_case:
    reason.append("Accident Case")
if pregnant:
    reason.append("Patient is Pregnant")
if chronic_disease:
    reason.append("Patient has Chronic Disease")
if 1 <= pain_scale <= 3:
    severity = "Mild"
elif 4 <= pain_scale <= 6:
    severity = "Moderate"
elif 7 <= pain_scale <= 10:
    severity = "Severe"
else:
    severity = "Invalid Input"
if arrival_mode:
    reason.append("Patient came in Ambulance")

if len(reason) ==0:
    print("Patient is Stable Condition")
else:
    print("Patient needs Urgent Attention")
    print("Reasons:")
    for r in reason:
        print("-", r)

if len(reason) == stable_condition:
    print("Patient is in Stable Condition")
elif reason == urgent_Condition:
    print("Patient needs urgent attention")
elif reason == critical_condition:
    print("Patient is in critical contition")
else:
    print("Patient can be discharged")
                                                                             