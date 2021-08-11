userInput = int(input("Input a positive integer here (that is not 1): "))
i = 0
threeXone = []

threeXone.append(userInput)
print(str(userInput))

def threeXPlusOneCounterOne(input, counter, list):
    counter = 0
    while input != 1:
        if input % 2 == 1:
            input *= 3
            input += 1
            print(input)
            list.append(input)
        else:
            input /= 2
            input = int(input)
            print(str(input))
            list.append(input)
        counter += 1

    counter = str(counter)
    print(f"\nThe number of operations is: {counter}")

def threeXPlusOneListLen(input, counter, list):
    while input != 1:
        if input % 2 == 1:
            input *= 3
            input += 1
            print(input)
            list.append(input)
        else:
            input /= 2
            input = int(input)
            print(str(input))
            list.append(input)
    counter = len(list)

threeXPlusOneCounterOne(userInput, i, threeXone)