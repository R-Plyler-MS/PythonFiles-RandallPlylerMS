movies = ['Scarface', 'Nutty Professor', 'Big Mommas House']

for magician in movies:
 print(magician.title())

for magician in movies:
 print(magician.title() + "was a great movie")

print("I really love movies!!!!!!!\n")

#part2
numbers = list(range(6,25))
print (numbers)
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

squares = []
for value in range(1,11):
	square = value*3
	squares.append(square)
print(squares)

#part3
squares = []
for value in range(1,11,):
	square = value**3
	squares.append(square)
print(squares)

squares = [value**3 for value in range(1, 11)]
print(squares)

#part4
movies = ['Scarface', 'Nutty Professor', 'Big Mommas House']
friend_movies = movies[:]
movies.append('Troy')
friend_movies.append('SavingPR')

print("\nmy favorite movies are")
for movie in movies:
	print(movie)
print("\nmy friends movies are")
for movie in friend_movies:
	print(movie)
	
#part5
candy = ('\nsnickers', 'almond joy', 'hershy', 'twix', 'milkdud')
for candies in candy:
	print(candies)
#candy[1] = 'skittles'

candy = ('\nskittles', 'starburst', 'hershy', 'twix', 'milkdud')
for candies in candy:
	print(candies)


# full_list = ['name1', 'name2', 'name3']
# for individual_item in full_list:
# 	print(individual_item)

# 	dimensions = (200, 50)
# print("Original dimensions")
# for dimension in dimensions:
# 	print(dimension)

# dimension = (400, 100)

# print("Modified dimensions")
# for dimension in dimensions:
# 	print(dimension)