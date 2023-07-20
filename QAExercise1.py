file = open('teams.txt', 'w')

file.writelines("TeamA " )
file.writelines("TeamB ")
file.writelines("TeamC ")
file.writelines("TeamD ")
file.writelines("TeamE")

file.close()

file = open("teams.txt", 'r')
teams = file.read()
teams = teams.split(' ')

print(teams[0],teams[3])