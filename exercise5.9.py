usernames = []
if usernames:
    for username in usernames:
        if username == 'asoka':
            print("Hello asoka, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
    print("new users in need!")
