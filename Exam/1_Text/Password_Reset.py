password = input()
text2 = ""

while True:
    data = input().split(" ")
    command = data[0]
    if command == "Done":
        break
    if command == "TakeOdd":
        for i in range(1, len(password), 2):
            text2 += password[i]
        password = text2
    if command == "Cut":
        substring = password[int(data[1]):(int(data[1])+int(data[2]))]
        password = password.replace(substring, "", 1)
    if command == "Substitute":
        if data[1] in password:
            password = password.replace(data[1], data[2])
        else:
            print("Nothing to replace!")
            continue
    print(password)
print(f"Your password is: {password}")
