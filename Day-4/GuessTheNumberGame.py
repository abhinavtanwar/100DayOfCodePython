import random

difficulty = input("Game difficulty easy or hard: ")
chosenNumber = random.randint(0, 100)

lives = 0

if difficulty.lower() == 'easy':
    lives = 10
else:
    lives = 5

flag = 0

while lives>0 and flag==0:
    print(f"Lives Remaining = {lives}")
    guess = int(input("Guess the number: "))
    if guess == chosenNumber:
        flag = 1
        print(f"You Won!!! The number was indeed {chosenNumber}")
    elif guess > chosenNumber:
        print("Too High")
        lives -= 1
    else:
        print("Too Low")
        lives -= 1