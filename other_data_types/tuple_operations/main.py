# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]
shelf1_update_tuple = tuple(shelf1_update)

#print(shelf1_update_tuple)
shelf1_concat = shelf1 + shelf1_update_tuple
#print(shelf1_concat)

celery_count=shelf1_concat.count("celery")
#print(celery_count)

celery_index=shelf1_concat.index("celery")
#print(celery_index)

print("Updated Shelf #1:", shelf1_concat)
print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)

print("################################################")

# Immutable configuration (tuples)
approved_branches = ("main", "release", "hotfix")
production_only_branch = ("main",)
active_environments = ("dev", "uat", "prod")

# Mutable configuration (lists)
authorized_roles = ["devops", "release-manager", "admin"]
blocked_ips = ["192.168.5.10", "10.1.1.7"]
restricted_commands = ["rm -rf /", "shutdown", "reboot"]
installed_packages = ["docker", "nginx", "python3", "terraform"]

user_role = "release-manager"
user_ip = "10.1.1.7"
current_branch = "feature-auth"
target_environment = "prod"
entered_command = "reboot"
required_packages = ["docker", "kubectl"]
build_id = "prod-build-701"

deployment_history = [
    "dev-build-501",
    "uat-build-620",
    "prod-build-700"
]
error = []

if user_role in authorized_roles:
    print("Authorized User")
else:
    print("User not Authorized")
    error.append("User not Permitted")

if user_ip in blocked_ips:
    print("User IP is Blocked")
    error.append("User IP is Blocked")
else:
    print("Valid IP Address")

if target_environment in active_environments:
    print("Valid Environment")
else:
    print("Invalid Environment")
    error.append("Invalid Environment")

if target_environment == "dev":
    print("DEV: Any branch permitted")
elif target_environment == "uat":
    if current_branch not in approved_branches:
        print("UAT: Only approved branches allowed")
        error.append("Invalid branch for UAT")
    else:
        print("UAT: Branch Approved")
elif target_environment == "prod":
    if current_branch not in production_only_branch:
        print("PROD: Only main branch allowed")
        error.append("Invalid branch for PROD")
    else:
        print("PROD: Branch Approved")
else:
    print("Invalid Environment for Branch Validation")

if entered_command in restricted_commands:
    print("Reboot Command not accepted")
    error.append("Reboot Command not accepted")

for package in required_packages:
    if package not in installed_packages:
        print(f"{package} is not installed")
        error.append(f"{package} not installed")
    else:
        print(f"{package} is installed")

build_exists = False

for existing_build in deployment_history:
    if existing_build == build_id:
        build_exists = True
        break

if build_exists:
    print("Build already deployed")
    error.append("Build already deployed")
else:
    print("New build - safe to deploy")
    
if len(error) == 0: 
    print("Deployment Successful")
    deployment_history.append(build_id) 
else:print("Deployment Failed")
print("Errors:", error)
    
