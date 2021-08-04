userInput = int(input("Input a positive integer here (that is not 1): "))
i = 0
threeXone = []

threeXone.append(userInput)
print(str(userInput))

while userInput != 1:
  if userInput % 2 == 1:
    userInput *= 3
    userInput += 1
    print(userInput)
    threeXone.append(userInput)
  else:
    userInput /= 2
    userInput = int(userInput)
    print(str(userInput))
    threeXone.append(userInput)
  i += 1

i = str(i)
print(f"\nThe number of operations is: {i}")
print(f"\n{threeXone}")