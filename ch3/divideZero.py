def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print("error: invalid argument")

print(spam(2)) # works
print(spam(12)) # works
print(spam(0)) # returns error