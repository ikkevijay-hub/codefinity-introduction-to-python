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
production_branch = "main"
target_environment = "prod"
entered_command = "docker build"
required_package = "docker"
build_id = "prod-build-311"
error=[]

if user_role not in authorized_roles:
    print("User not role Authorised")
    error.append("User not Authorised")
else:
    print("User Role Authorised")
        
if user_ip in blocked_ips:
    print("User IP in Blocked IPs")
    error.append("User IP in Blocked IPs")
else:
    print("Valid Ip address")
        
if production_branch not in approved_branches:
    print("Feature Branch not permitted")
    error.append("Feature Branch not permitted on PROD")
elif production_branch in approved_branches:
    print("Main Branch Deployment approved")
else:
    print("Only main Brach permitted for deployment")
    
    
if entered_command not in restricted_commands:
    print("Docker build is permitted")
else:
    print("Docker build not Permitted")
    error.append("Docker build not Permitted")

if target_environment in active_environments:
    print("Prod Environment in Active Environment")
else:
    print("Prod Environment not in Active Environment")
    error.append("Prod Environment not in Active Environment")
    
if required_package in installed_packages:
    print("Package is Already installed")
else:
    print("Package not installed")
    error.append("Package not Permitted to be instaled")

if build_id not in deployment_history:
    print("Develoyment not in History")
    error.append("prod-build-311 not in Develoyment History")
else:
    print("prod-build-311 is already Deployed")
    
if len(error) == 0:
    print("Deployment Successful")
    #deployment_history.append(build_id)
else:
    print("Deployment Failed")
    print("Errors:", error)





    

    
    



    


