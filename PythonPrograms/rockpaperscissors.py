import random

comp_input= random.choice (['rock','paper','scissors'])
user_input= input ("Enter either rock, paper or scissors \n")

print ("Computer input is: " + comp_input)
if comp_input == user_input:
    print ("It's a TIE")
elif user_input == "rock" and comp_input == "scissors":
    print ("User wins")
elif user_input == "paper" and comp_input == "rock":
    print ("User wins")
elif user_input == "scissors" and comp_input == "paper":
    print ("User wins")
else:
    print ("Computer wins")
