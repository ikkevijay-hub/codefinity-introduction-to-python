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
allowed_environments = ("dev", "test", "prod")
allowed_project_types = ("web", "api", "mobile")
production_branches = ("main",)

#Mutable Configuration (Lists)
approved_test_branches = ["main", "release", "hotfix"]
authorized_roles = ["developer", "qa", "manager", "admin"]
blocked_users = ["user300", "user404"]
restricted_actions = ["delete-db", "force-push", "server-shutdown"]
installed_services = ["docker", "nginx", "redis", "postgres"]

#Dictionary Configuration 
user_database = {
    "user101": {"role": "developer", "department": "engineering"},
    "user202": {"role": "manager", "department": "engineering"},
    "user300": {"role": "qa", "department": "testing"},
}

environment_limits = {
    "dev": 5,
    "test": 3,
    "prod": 1
}

#Incoming Deployment Request
username = "user300"
project_name = "api-payment-v2"
project_type = "api"
target_environment = "prod"
current_branch = "feature-payment"
requested_action = "force-push"
required_services = ["docker", "kubernetes"]
number_of_instances = 2

error=[]

if username in user_database:
    print("User Permitted")
else:
    print("User not in User Database")
    error.append("User not in User Database")

print("##############")

if username not in blocked_users:
    print("User Name not in Blocked User List")
else:
    print("User Name in Blocked User List")
    error.append("User Name in Blocked User List")

print("##############")

if username in user_database:
    user_role = user_database[username]["role"]
    if user_role in authorized_roles:
        print("User Role is Authorized")
    else:
        print("User Role Not Authorized")
        error.append("User Role Not Authorized")

print("##############")

if project_type not in allowed_project_types:
    print("Project Type not Allowed")
    error.append("Project Type not Allowed")
else:
    print("Project Type Allowed")

print("##############")

if target_environment not in allowed_environments:
    print("Target Environment not in Allowed Environment")
    error.append("Target Environment not in Allowed Environment")
else:
    print("Target Environment in Allowed Environment")

print("##############")

if target_environment == "dev":
    print("DEV-Can Deploy any Branch")    
elif target_environment == "test":
    if current_branch not in approved_test_branches:
        print("Test- Invalid Branches for test ")
        error.append("Test-Invalid Branches for test")    
elif target_environment == "prod":
    if current_branch not in production_branches:
        print("PROD-Can Deploay Approved Branches")
        error.append("PROD-Can Deploay Approved Branches")
else:
    print("Deployment Not allowed")

print("##############")

if requested_action in restricted_actions:
    print("Force Push Not Permitted ")
    error.append("Force Push Not Permitted ")
    
print("##############")

for service in required_services:
    if service not in installed_services:
        print("Service Not in Installed Service")
        error.append(f"{service} not in installed service")
    else:
        print(f"{service} in installed service")

print("##############")

limit = environment_limits[target_environment]

if target_environment == "dev":
    if number_of_instances > limit:
        print("Dev Environment Exceeded Limit")
        error.append("Dev Environment Exceeded Limit")
if target_environment == "test":
    if number_of_instances > limit:
        print("Test Environment Exceeded Limit")
        error.append("Test Environment Exceeded Limit")
if target_environment == "prod":
    if number_of_instances > limit:
        print("Prod Environment Exceeded Limit")
        error.append("Prod Environment Exceeded Limit")

print("##############")

if len(error) == 0:
    print("Deployment Approved")
else:
    print("Deployment Rejected")
    print("Error :", error)



#Immutable Configuration (Tuples)
allowed_environments = ("dev", "test", "stage", "prod")
allowed_project_types = ("web", "api", "mobile", "data")
production_only_branches = ("main", "release")
sensitive_environments = ("stage", "prod")

#Mutable Configuration (Lists)
approved_test_branches = ["main", "develop", "release"]
authorized_roles = ["developer", "qa", "manager", "admin"]
blocked_users = ["user900", "user404"]
restricted_actions = ["force-delete-db", "shutdown-server"]
installed_tools = ["docker", "git", "nginx", "postgres"]
required_tools = ["docker", "git", "kubernetes"]

#Dictionary Configuration (Database Style Data)
user_database = {
    "user101": {"role": "developer", "department": "engineering"},
    "user202": {"role": "manager", "department": "engineering"},
    "user303": {"role": "qa", "department": "testing"},
    "user900": {"role": "developer", "department": "engineering"}
}

environment_limits = {
    "dev": 5,
    "test": 3,
    "stage": 2,
    "prod": 1
}

project_registry = {
    "payment-api": {"type": "api", "owner": "user101"},
    "frontend-app": {"type": "web", "owner": "user202"},
    "analytics-data": {"type": "data", "owner": "user303"}
}

#Incoming Dynamic Deployment Request
#(These should be passed dynamically into functions 👇)

username = "user101"
project_name = "payment-api"
target_environment = "prod"
current_branch = "feature-payment"
requested_action = "force-delete-db"
number_of_instances = 2

def validate_user(username):
    if username == "user101":
        print("Valid user")