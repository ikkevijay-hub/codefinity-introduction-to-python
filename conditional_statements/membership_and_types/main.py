# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

# Write your code here



#print("Contains 'raw':", contains_raw)
#print("Contains 'Imported':", contains_Imported)
#print("Is price a float?:", price_is_float)
#print("Is count an integer?:", count_is_int)

# Requirements:
# - Check if user_role has access
# - Check if user_ip is blocked
# - Check if target_environment is valid

allowed_roles = ["admin", "devops", "auditor"]
blocked_ips = ["192.168.1.10", "10.0.0.5", "172.16.0.9"]
active_environments = ("dev", "uat", "prod")

user_role = "devops"
user_ip = "10.0.0.5"
target_environment = "prod"

error=[]

if user_role not in allowed_roles:
    print("User access Blocked")
    error.append ("Invalid Role")

if user_ip  in blocked_ips:
    print("User IP is blocked")
    error.append ("Blocked IP")
    
if target_environment not in active_environments:
    print("Environment Not in Active Status")
    error.append("Invalid Environment")

if len(error) == 0:
    print("Valid User")
else:
    print("Invalid User")
    print("Errors:", error)
 