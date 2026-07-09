from recommendation import get_projects

career = "ML Engineer"

projects = get_projects(career)

print("=" * 40)
print("Recommended Projects")
print("=" * 40)

for project in projects:
    print("•", project)