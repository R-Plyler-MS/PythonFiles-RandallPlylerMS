message = "Hello  Python World"
print(message)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1].title())
bicycles.append('ducati')
print(bicycles)
bicycles.insert(0, 'schwinn')
print(bicycles)
del bicycles[3]
print(bicycles)
popped_bicycle = bicycles.pop()
print(popped_bicycle)
first_owned = bicycles.pop(0)
print(f"The first bicycle I owned was a {first_owned.title()}")

motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)


