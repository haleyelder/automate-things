# break in while loop
while True:
    print("please print your name")
    name = input()
    # only stops if enter in "your name" exactly
    if name == "your name":
        break
    print("Thank you")