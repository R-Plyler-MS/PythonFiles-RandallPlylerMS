prompt = "\nPlease enter the name of a city you have visited"
prompt += "\n(Enter 'quit' when you are finished.) "

while true:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"I love to go to the {city.title}")




current_number = 0
while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue
    print(current_number)
