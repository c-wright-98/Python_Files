file = open("teams.txt", "w")
file.writelines("This is a new line")

file = open("teams.txt", "r")
Lines = file.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print(line)