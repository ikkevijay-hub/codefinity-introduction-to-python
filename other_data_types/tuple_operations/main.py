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

if active_environments in approved_branches:
    print(" ")