start_number = 5
countdown_values = []

current = start_number
while current >= 1:
    countdown_values.append(current)
    current -= 1

print("Discount countdown complete!")
print(countdown_values)

print("##############################################################")

#Immutable Configuration (Tuples)
allowed_departments = ("engineering", "finance", "hr")
admin_roles = ("admin", "superadmin")
restricted_features = ("delete-user", "modify-salary")
#Mutable Data (Lists)
blocked_users = ["user900", "user404"]
logged_in_users = ["user101", "user202"]
#Dictionary (Database)
user_database = {
    "user101": {"role": "developer", "department": "engineering"},
    "user202": {"role": "manager", "department": "finance"},
    "user303": {"role": "hr", "department": "hr"},
}
#Dynamic Request
username = "user202"
requested_feature = "modify-salary"

error=[]

def validate_user(username, requested_feature):
    
    if username not in user_database:
        print("User Name not in User Database")
        error.append("User Name not in User Database")
        return
    
    print("User Name in User Database")

    if username in blocked_users:
        print("User in Blocked User List")
        error.append("User in Blocked User List")
    else:
        print("User not in Blocked User List")

    if username not in logged_in_users:
        print("User Not Logged in")
        error.append("User Not Logged in")
    else:
        print("User Logged in")

    # Correct way: check department
    user_department = user_database[username]["department"]

    if user_department not in allowed_departments:
        print("User Department not allowed")
        error.append("User Department not allowed")
    else:
        print("User Department allowed")

    # Restricted feature logic
    if requested_feature in restricted_features:
        user_role = user_database[username]["role"]
        
        if user_role not in admin_roles:
            print("Only admin can access restricted feature")
            error.append("Restricted feature not allowed")
        else:
            print("Admin access granted")
    else:
        print("Feature is not restricted")
print(validate_user(username, requested_feature))
          
if len(error) == 0:
    print("user can access a system feature")
else:
    print("user cannnot access a system feature")
    print("Error :", error)

print("###################################")

#Tuples
mandatory_tools = ("docker", "git", "kubernetes")
optional_tools = ("helm", "terraform")
#Lists
installed_tools = ["docker", "git"]
failed_tools = []
#Dictionary
environment_requirements = {
    "dev": {"min_tools": 2},
    "prod": {"min_tools": 3}
}
#Dynamic Request
target_environment = "prod"

error=[]

count = 0

for tool in mandatory_tools:
    if tool in installed_tools:
        print(f"{tool} is installed")
        count += 1
    else:
        print(f"{tool} is NOT installed")
        error.append(f"{tool} is NOT installed")

if target_environment in environment_requirements:
    min_required = environment_requirements[target_environment]["min_tools"]

    if count >= min_required:
        print(f"{target_environment} requirement satisfied")
    else:
        print(f"{target_environment} requirement NOT satisfied")
        error.append(f"{target_environment} requirement NOT satisfied")
else:
    print("Unknown environment")
    error.append("Unknown environment")

if len(error) == 0:
    print("deployment can proceed based on installed tools.")
else:
    print("deployment cannot proceed based on installed tools.")
    print("Error :", error)

print("###################################")

