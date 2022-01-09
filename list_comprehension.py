squares = [value**2 for value in range(1, 11)]
print(squares)

players = ['charles', 'fredrick', 'buba', 'florence', 'chucknorris']
print(players[0])
print(players[0:3])


for player in players[:3]:
	print(player.title())

my_foods = ['pizza', 'chips', 'jerky']
print(my_foods)

dimensions = (200, 50)
print("Original dimensions")
for dimension in dimensions:
	print(dimension)

dimension = (400, 100)

print("Modified dimensions")
for dimension in dimensions:
	print(dimension)



dimensions[0]
