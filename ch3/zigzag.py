import time, sys
indent = 0 # spaces to indent
indentIncreasing = True # if indent is increasing or not

try:
    while True: # main program
        print(' ' * indent, end="")
        print("********")
        time.sleep(0.1) #pause for 1/10 second

        if indentIncreasing:
            # if indents increasing
            indent = indent +1
            # return false to change direction
            if indent == 7:
                indentIncreasing = False

        else: 
            indent = indent -1
            if indent == 0:
                # change direction
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()