file = open("teams.txt", "r")
print(file.readlines())

file = open("teams.txt", "w")
file.writelines("This is a new line")
file.close()

file = open("teams.txt", "r")

print(file.readlines(10))