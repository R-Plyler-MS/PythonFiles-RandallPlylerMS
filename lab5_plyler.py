list1 = ['Star Wars', 'LOTR', 'Twilight', 'Dumbo', 'Peter Pan']
list2 = [1,2,3,4,5]

if list1[0] != list1[1]:
	print("The values are not equal.")

if list1[0].lower() == "star wars":
	print("Star Wars is one of your favorite movies")

if list2[0] == list2[1]:
	print("PRINT THIS")

if list2[0] <= list2[1]:
	print("PRINT THIS less than")

if list2[0] >= list2[1]:
	print("PRINT THIS equal than")

if list2[0] != list2[1]:
	print("The first movie is not the same as the second")

if list2[0] < list2[1] and list2[0] < list2[2]:
	print("This works too")

if list2[0] < list2[1]:
	print("First value is less than the second")

if (list2[0] < list2[1]) or (list2[2] > list2[3]):
	print("This is printing")

if 1 in list2 or (list2[2] > list2[3]):
	print("Nice Calculation")

if 'Star Wars' in list1:
	print("IT IS!")

if 'Superman' not in list1:
	print("ITS NOT!")


alien_color = "Yellow"

if alien_color == "Green":
	print("you just earned 5 points")
if alien_color == "Yellow":
	print("you just earned 5 points")

alien_color = "Yellow"

if alien_color == "green":
	print("You just earned 5 points")
else:
	print("You just earned 10 points")

if alien_color == "yellow":
	print("You just earned 5 points")
else:
	print("You just earned 50000000 points")


alien_color = "Green"

if alien_color == "Green":
	print("The Alien is Green, 5 points")
elif alien_color == "Yellow":
	print("The Alien is Yellow, 10 points")
elif alien_color == "Red":
	print("The Alien is Red, 15 points")

alien_color = "Yellow"

if alien_color == "Green":
	print("The Alien is Green, 5 points")
elif alien_color == "Yellow":
	print("The Alien is Yellow, 10 points")
elif alien_color == "Red":
	print("The Alien is Red, 15 points")

alien_color = "Red"

if alien_color == "Green":
	print("The Alien is Green, 5 points")
elif alien_color == "Yellow":
	print("The Alien is Yellow, 10 points")
elif alien_color == "Red":
	print("The Alien is Red, 15 points")

favorite_foods = ['chicken', 'rice', 'lima beans']

for favorite_food in favorite_foods:
	if favorite_food == 'carrots':
		print("You Love Carrots")
	elif favorite_food == 'chicken':
		print("You love chicken, CHICKEN!!!!!!!!")
	elif favorite_food == 'turnips':
		print("Who eats turnips?!")
	elif favorite_food == 'lima beans':
		print("Youre sick for liking lima beans")
	elif favorite_food == 'rice':
		print("plane jane loves rice")
