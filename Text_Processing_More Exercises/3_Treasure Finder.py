secret = [int(x) for x in input().split()]


while True:
    message = input()
    if message == "find":
        break
    decrypted_message = ""
    for i in range(len(message)):
        current_el = ord(message[i]) - secret[i % len(secret)]
        decrypted_message += chr(current_el)
    first_start = decrypted_message.index("&")
    first_end = decrypted_message.rindex("&")
    second_start = decrypted_message.index("<")
    second_end = decrypted_message.rindex(">")

    print(f"Found {decrypted_message[first_start +1:first_end]} at {decrypted_message[second_start +1:second_end]}")
