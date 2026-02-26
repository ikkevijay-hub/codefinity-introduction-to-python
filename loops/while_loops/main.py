start_number = 5
countdown_values = []

current = start_number
while current >= 1:
    countdown_values.append(current)
    current -= 1

print("Discount countdown complete!")
print(countdown_values)

print("##############################################################")

Immutable Configuration (Tuples)
allowed_environments = ("dev", "test", "prod")
allowed_project_types = ("web", "api", "mobile")
production_branches = ("main",)

Mutable Configuration (Lists)
approved_test_branches = ["main", "release", "hotfix"]
authorized_roles = ["developer", "qa", "manager", "admin"]
blocked_users = ["user300", "user404"]
restricted_actions = ["delete-db", "force-push", "server-shutdown"]
installed_services = ["docker", "nginx", "redis", "postgres"]

Dictionary Configuration 
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

Incoming Deployment Request
username = "user300"
project_name = "api-payment-v2"
project_type = "api"
target_environment = "prod"
current_branch = "feature-payment"
requested_action = "force-push"
required_services = ["docker", "kubernetes"]
number_of_instances = 2



    