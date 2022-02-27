# says hello and ask for name!

print("hello!")
print("what is your name?")
# ask for name
myName = input()
print("it's good to meet you, " + myName)
print("The length of your name is: ")
# length of input name len()
print(len(myName))
print("what is your age?")
myAge = input()
# add 1 to current age and stringify to output in sentence
print("You will be " + str(int(myAge) + 1) + ' in a year.')
