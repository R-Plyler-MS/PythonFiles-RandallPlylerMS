#3-1
names = ['randy', 'derek', 'eric']
print(names)

#3-2
print(names[1], 'likes python')

#3-4
dinner_list = ['gma', 'gpa', 'unclebob']
print('I would like to invite', dinner_list[0], dinner_list[1], 'and',dinner_list[2],'to dinner')

#3-5
print('uncle bob cannot make it to the dinner tonight')
del dinner_list[2]
print('the new list of people coming are', dinner_list[0], dinner_list[1])

#3.6
print('We found a bigger table!!!!!!!!!!')
dinner_list.insert(0, 'Davy Crocket')
dinner_list.insert(2, 'Ernest Shackelton')
dinner_list.append('Michael Jordan')
print(f"Please come to my party, {dinner_list[0].title()}")
print(f"Please come to my party, {dinner_list[1].title()}")
print(f"Please come to my party, {dinner_list[2].title()}")
print(f"Please come to my party, {dinner_list[3].title()}")
print(f"Please come to my party, {dinner_list[4].title()}")

#3.7
print("unfortunatly I can only invite two people for dinner.")
popped_dinner_list = dinner_list.pop()
print(f"{popped_dinner_list}, you're uninvited from the party")
popped_dinner_list = dinner_list.pop()
print(f"{popped_dinner_list}, you're uninvited from the party")
popped_dinner_list = dinner_list.pop()
print(f"{popped_dinner_list}, you're uninvited from the party")

#3.8
places = ['iraq', 'somolia', 'south sudan', 'kazakhstan', 'north korea']
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

places.sort(reverse=False)
print(places)

#3.9
names = ['donald', 'joe']
list_length = len(names)
print(f"There are {list_length} names in this list")

