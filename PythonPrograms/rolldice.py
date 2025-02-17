import random
roll = random.randint (1,6)

guess = int (input("Guess the rolled number: \n"))

if guess == roll:
    print ("correct, they rolled: " + str(roll))

else:
    print ("Incorrect guess")
