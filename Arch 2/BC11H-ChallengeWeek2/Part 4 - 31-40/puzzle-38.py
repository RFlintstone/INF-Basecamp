from itertools import combinations
from Challenge_Resources.ict_skills import skills1

wishlist = {"Python", "SQL", "Java", "Blockchain"}

# Generate all possible combinations of team members
team_combinations = list(combinations(skills1.keys(), 3))

# Count how many teams meet the wishlist
count = 0
for team in team_combinations:
    team_skills = set()
    for member in team:
        team_skills.update(skills1[member])
    if wishlist.issubset(team_skills):
        count += 1

print(f"Number of different teams with the specified skills: {count}")

# RESULT: 5151
