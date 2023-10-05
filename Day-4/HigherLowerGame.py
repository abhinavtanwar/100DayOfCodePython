import Objects as ob
import os
import time

p1 = ob.giveObject()
p2 = ob.giveObject()

score = 0
flag = 0

while flag == 0:
    os.system('cls')
    print(f"Current Score = {score}")
    print(f"A: {p1['name']}, a {p1['description']} from {p1['country']}")
    print(f"B: {p2['name']}, a {p2['description']} from {p2['country']}")

    guess = input("Guess who has more Instagram followers A or B: ").lower()

    if p1['follower_count'] > p2['follower_count']:
        greatest = 'a'
    elif p2['follower_count'] > p1['follower_count']:
        greatest = 'a'
    else:
        greatest = 'Draw'

    if greatest == 'Draw':
        print("It's a draw, you don't lose but no point...")
    elif guess == greatest:
        print("CORRECT!!!")
        score += 1
        p1 = p2
        p2 = ob.giveObject()
        time.sleep(0.5)
    else:
        print(f"You Lose, Final Score = {score}")
        flag = 1
    