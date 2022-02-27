while True:
    print("who are you?")
    # ask user input
    name = input()
    # repeat ask if answer is not joe
    if name != "Joe":
        continue
    print("hello, joe, what is the password? (it is a fish)")
    password = input()
    # if word is anything but swordfish, print access granted
    if password == "swordfish":
        break
print("access granted")