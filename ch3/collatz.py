# part 1
# def collatz(number):
#     if (number % 2 == 0):
#         print(number // 2)
#     elif(number % 1 == 0):
#         print(3 * number + 1)
    
# collatz(34)

# part 2 
while True:
    print("Enter Number")
    inputNum = input()
    # until input matches 1 (stringified); keep asking, then break loop
    if inputNum == str(1):
        break
    print("end")
