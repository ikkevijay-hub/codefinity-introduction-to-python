vegetables = ["tomatoes", "potatoes", "onions"]

if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

vegetables.remove("onions")
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)

print("#############################################################")

pipeline_stages = ["build", "test", "scan"]
failed_stages = []
approved_environments = ["dev", "uat"]
deployment_history = ["dev-build-001", "uat-build-002"]

new_stage = "deploy"
environment = "prod"
new_build = "prod-build-003"

          
pipeline_stages.insert(3,new_stage)
print(pipeline_stages)
pipeline_stages.remove("scan")
print(pipeline_stages)
pipeline_stages.sort()
print(pipeline_stages)
if environment not in approved_environments:
    failed_stages.append("environment")
print(approved_environments)
deployment_history.insert(2, new_build)
print(deployment_history)
pipeline_stages.reverse()
print(pipeline_stages)
deployment_history.remove("dev-build-001")
print(deployment_history)
approved_environments.copy()
print(approved_environments.copy())
pipeline_stages.count("deploy")
print(pipeline_stages.count("deploy"))
pipeline_stages.index("test")
print(pipeline_stages.index("test"))

print("#############################################################")

approved_branches = ["main", "release", "hotfix"]
restricted_commands = ["rm -rf /", "shutdown", "reboot", "kill -9"]
authorized_roles = ["devops", "release-manager", "admin"]
blocked_ips = ["192.168.10.15", "10.0.0.8"]
active_environments = ["dev", "uat", "prod"]
installed_packages = ["docker", "nginx", "python3", "terraform"]

deployment_history = [
    "dev-build-101",
    "uat-build-205",
    "prod-build-310"
]

user_role = "devops"
user_ip = "10.0.0.8"
current_branch = "feature-payment"
target_environment = "prod"
entered_command = "docker build"
required_package = "docker"
build_id = "prod-build-311"
error=[]
development_successfull = error in [approved_branches, authorized_roles, 
                           blocked_ips, active_environments,installed_packages]
development_failed = error not in [approved_branches, authorized_roles, 
                           blocked_ips, active_environments,installed_packages]

if user_role in authorized_roles:
    print("User Role Authorised")
else:
    print("User not Authorised")
    error.append("User not Authorised")
if user_ip in blocked_ips:
    print("User IP in Blocked IPs")
else:
    print("Valid Ip address")
    error.append("User IP in Blocked IPs")
if current_branch not in approved_branches or current_branch in approved_branches:
    print("Feature Branch not permitted")
else:
    print("Only main Brach permitted for deployment")
    error.append("Feature Branch not permitted on PROD")
if entered_command not in restricted_commands:
    print("Docker build is permitted")
else:
    print("Docker build not Permitted")
    error.append("Docker build not Permitted")
active_environments.append(target_environment)
print(active_environments)
installed_packages.append(required_package)
print(installed_packages)

if build_id in deployment_history:
    print("prod-build-311 not in Develoyment History")
else:
    print("prod-build-311 is already Deployed")
    error.append("prod-build-311 not in Develoyment History")

if development_successfull and build_id:
    print("Deployment Successful + build_id history")
    error.append == 0
    print(error)
elif development_failed and error:
    print("Deployment failed")
    error.append == 0
    print(error)
else:
    print("Deplyment Needs to be rescheduled")





    

    
    



    


