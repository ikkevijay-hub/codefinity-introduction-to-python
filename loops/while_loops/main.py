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

error=[]

def validate_user(username):
    if username in user_database:
        print("Valid user")
    else:
        print("Invalid user")
        error.append("Invalid user")
    if username not in blocked_users:
        print("User not in Blocked User List")
    else:
        print("User in Blocked User List")
        error.append("User in Blocked User List")
    if username in user_database:
        user_role = user_database[username]["role"]
    if user_role in authorized_roles:
        print("User Role is Authorized")
    else:
        print("User Role not Authorized")

print(validate_user("user101"))

def project_type (project_name):
    if project_type in project_registry:
        print("Project found in registry")        
    else:
        print("Project not found in registry")
        error.append("Project not found in registry")
        
def project_info (project_registry):
    if project_info in allowed_project_types:
        print("Project type permitted")
    else:
        print("Project type not permitted")
        
print(project_type("payment-api"))
print(project_info("payment-api"))


#print("Errors:", error)


