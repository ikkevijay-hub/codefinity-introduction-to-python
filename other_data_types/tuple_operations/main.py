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

deployment_history = [
    "dev-build-501",
    "uat-build-620",
    "prod-build-700"
]

error = []

