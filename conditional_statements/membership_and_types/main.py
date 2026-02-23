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

print("################################################")
# Write conditions to check:
# - Is deployment allowed from this branch?
# - Is the command restricted?
# - Is the package installed?

approved_branches = ["main", "release", "hotfix"]
restricted_commands = ["rm -rf /", "shutdown", "reboot"]
installed_packages = ["nginx", "docker", "python3"]
target_environment = "prod"

current_branch = "feature-login"
entered_command = "shutdown"
package_to_check = "docker"

error=[]

if current_branch not in approved_branches:
    print("Feature Login Branch not included")
    error.append("Incorrect Branch")

if target_environment == "prod":
    if current_branch == "main":
        print("Production Deployment Allowed ✅")
    else:
        print("Only main branch can deploy to production ❌")
else:
    print("Non-production deployment allowed")
    

if entered_command in restricted_commands:
    print("Shutdown is Not Allowed")
    error.append("Shutdown Disabled")

if package_to_check in installed_packages:
    print("Packed is Installed")
    error.append("Package Installed")

if len(error) == 0:
    print("DevOps Deployment Validated")
else:
    print("DevOps Deployment Failed")
    print("Errors:", error)

 