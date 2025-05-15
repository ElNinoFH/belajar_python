goal_list = ["Python", "HTML", "CSS"]
goal_list += ["Database", "Django"]

file = open("file a.txt", "a")
file.write("\n")
for goal in goal_list:
    file.write(f"Master {goal}\n")
file.close