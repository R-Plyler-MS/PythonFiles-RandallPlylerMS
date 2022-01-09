#Assignment 2

import random


#Part1)

print("\nPart 1\n")
music_artists = ['ACDC', 'Pink Floyd', 'Queen']
print(music_artists)
music_artists.append('Michael Jackson')
print(music_artists)
music_artists[1] = "Prince"
print(music_artists)

print("\n")

for music_artist in music_artists:
	print(music_artist.title(), 'is a great artist')
print("\n")
second_list_music = music_artists

music_artists.append('Tom Petty')
print(music_artists)
del second_list_music[4]
second_list_music.append('Van Hallen')
print(second_list_music)

print("\nPart 2\n")


#Part2)

random_number_list = []
for LoopB in range(1, 11):
	random_number_list.append(random.randint(1,100))


print(random_number_list,)
print("\nThis is the min in the list --->", min(random_number_list))
print("\nThis is the max in the list --->", max(random_number_list))
print("\nThis is the sum in the list --->", sum(random_number_list))
print("\nThis are the first four numbers --->", random_number_list[:4])



listA = random_number_list
random_number_list = listA


print("\nThese are the numbers multiplied by 5 in one line")
total_each = [i * 5 for i in random_number_list]


print(total_each)
print("\n")

#Part3)

print("Part 3\n")
print("These are the random numbers, \n\n", random_number_list, "\n")
for varA in random_number_list: 
    
    if varA % 2 == 0: 
       print("These are the even numbers", varA) 

print("\n")
for varA in random_number_list: 
   
    if varA % 2 != 0:
    	print("These are the odd numbers", varA)

print("\n")

Even_numbers = 0
Odd_numbers = 0
  
for LoopC in random_number_list:  
    
    if LoopC % 2 == 0: 
       
        Even_numbers += 1

    else: 
       
        Odd_numbers += 1

print("There are", Even_numbers, "in the list.") 
print("There are", Odd_numbers, "in the list.") 
print("\n")
