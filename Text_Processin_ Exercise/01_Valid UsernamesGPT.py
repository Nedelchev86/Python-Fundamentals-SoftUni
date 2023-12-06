import re

def is_valid_username(username):
    # Check length
    if len(username) < 3 or len(username) > 16:
        return False

    # Check allowed characters
    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        return False

    # Check for redundant symbols
    if re.match(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', username):
        return False
    if re.search(r'[^a-zA-Z0-9]{2,}', username):
        return False

    return True

# Read usernames from a single line
usernames = input().split(", ")

# Print valid usernames
for username in usernames:
    if is_valid_username(username):
        print(username)
