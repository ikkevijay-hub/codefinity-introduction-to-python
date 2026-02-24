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

#User role authorized_roles मध्ये असावा.
#User IP blocked_ips मध्ये नसावा.
#Production deployment फक्त "main" branch वरून होईल.
#entered_command restricted_commands मध्ये नसावा.
#target_environment active_environments मध्ये असावा.
#required_package installed_packages मध्ये असावा.
#build_id deployment_history मध्ये नसावा.
#जर कोणताही rule fail झाला → Deployment Failed + errors list print करा
#सगळं valid असेल → Deployment Successful + build_id history मध्ये add करा

if user_role not in authorized_roles:
    print


