activation_key = input()
while True:
    command = input()
    if command == 'Generate':
        break
    data = command.split('>>>')
    substring = data[1]
    if data[0] == 'Contains':
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif data[0] == 'Flip':
        if data[1] == 'Upper':
            start, end = int(data[2]), int(data[3])
            activation_key = activation_key[:start] + activation_key[start:end].upper() + activation_key[end:]
        elif data[1] == 'Lower':
            start, end = int(data[2]), int(data[3])
            activation_key = activation_key[:start] + activation_key[start:end].lower() + activation_key[end:]
        print(activation_key)
    elif data[0] == 'Slice':
        start, end = int(data[1]), int(data[2])
        activation_key = activation_key[:start] + activation_key[end:]
        print(activation_key)
print(f"Your activation key is: {activation_key}")