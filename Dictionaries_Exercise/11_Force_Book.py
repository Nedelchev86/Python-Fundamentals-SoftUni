force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        user_is_part = False
        for value in force_book.values():
            if force_user in value:
                user_is_part = True
                break
        if not user_is_part:
            if force_side not in force_book.keys():
                force_book[force_side] = [force_user]
            else:
                force_book[force_side].append(force_user)
    elif " -> " in command:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]
        for key, value in force_book.items():
            if force_user in value:
                force_book[key].pop(value.index(force_user))
                break
        if force_side not in force_book.keys():
            force_book[force_side] = [force_user]
        else:
            force_book[force_side].append(force_user)
        print(F"{force_user} joins the {force_side} side!")

for force, users in force_book.items():
    if len(users) > 0:
        print(F"Side: {force}, Members: {len(users)}")
        for user in users:
            print(F"! {user}")