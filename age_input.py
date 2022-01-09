
prompt = "Tell me your first name: "
prompt += "\n Enter first name"




name = input(prompt)
print(f"Hello, {name}")


age = int(input("How old are you"))

if age >= 18 and age <= 100:
    print("You are old enough to vote")
elif age > 100:
    print("You are not old enough")
else:
    print("You are too young.")

for num in range(1,6):
    print(num)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

while message != "Quit":
    message = input(prompt)
    print(message)