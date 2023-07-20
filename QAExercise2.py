file = open("teams.txt", "w")
file.writelines("This is a new line")

file = open("teams.txt", "r")

print(file.readlines())