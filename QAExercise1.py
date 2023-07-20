file = open('teams.txt', 'w')

file.write("TeamA " )
file.write("TeamB ")
file.write("TeamC ")
file.write("TeamD ")
file.write("TeamE")

file = open("teams.txt", 'r')
teams = file.read()
teams = teams.split(' ')

print(teams[0],teams[3])