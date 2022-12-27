# Make a two-player Rock-Paper-Scissors game. 
import random

def win():
    print("You win!")

def lose():
    print("You lose!")

def convert(value):
    if value == 0:
        return "rock"
    elif value == 1:
        return "paper"
    else:
        return "scissors"


print("This is a rock-paper-scissors game. ")

z = input("rock/paper/scissors?: ")

y = convert(random.randint(0,2))

print(f"computer chose {y}")

if y == z:
    print("we have a tie!")

if z == "rock":
    if y == "scissors":
        print("rock beats scissors.")
        win()
    else:
        print("paper beats rock.")
        lose()

if z == "paper":
    if y == "rock":
        print("paper beats rock.")
        win()
    else:
        print("scissors beats paper.")
        lose()

if z == "scissors":
    if y == "paper":
        print("scissors beats paper.")
        win()
    else:
        print("rock beats scissors.")
        lose()