from roadmap import get_roadmap

career = "ML Engineer"

roadmap = get_roadmap(career)

print("=" * 40)
print("Learning Roadmap")
print("=" * 40)

for week in roadmap:
    print(week)