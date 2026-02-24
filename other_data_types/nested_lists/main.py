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







