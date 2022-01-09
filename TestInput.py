unconfirmed_users = ['alice', 'brian']
confirmed_users = []


while unconfirmed_users:
    current_user = unconfirmed_users[0]
    del unconfirmed_users[0]

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)


for unconfirmed_users in unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)


print("\nThe following users have been confirmed:")
for confirmed_users in confirmed_users:
    print(confirmed_users.title())
