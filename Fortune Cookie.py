import random

print(random.randint(1,10))
# This will give me a random number from 1-10

print(random.random())
# This will give me a random number from 0-1

#This next project is to make a magic 8 ball that will give you 5 different answers

answer = random.randint(1,5)

if answer == 1:
    print("Yes")
if answer == 2:
    print("No")
if answer == 3:
    print("Sorry, I don't think so!")
if answer == 4:
    print("Hmm...try again")
if answer == 5:
    print("you must seek from within for your answer")
