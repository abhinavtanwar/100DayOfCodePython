import random
import os
import time

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer = []

#initial deal
def deal():
    player.append(random.choice(cards))
    player.append(random.choice(cards))
    computer.append(random.choice(cards))
    computer.append(random.choice(cards))

# when player hits hit
def playerhit():
    drawncard = random.choice(cards)
    player.append(drawncard)
    print(f"You drew {drawncard}")

def computerhand():
    # checking computer sum
    sum = 0
    for i in computer:
        sum+= i
    
    # if sum<16 computer must draw a card
    while sum<16:
        drawncard = random.choice(cards)
        computer.append(drawncard)
        sum += drawncard
        if checkGameOver(computer):
            break

# Check whether game is still going or not
def checkGameOver(poc):
    #finding the total sum of the hand
    sum = 0
    for i in poc:
        sum += i
    
    if poc == player:
        if sum == 21:
            print("BlackJack!! You Win...")
            return True
        if sum > 21:
            print("You Lose")
            return True
        else:
            return False
    else:
        if sum == 21:
            print("Computer BlackJack!! You Lose...")
            return True
        if sum > 21:
            print("You Win")
            return True
        else:
            return False


# checking for the winner
def Winner():
    psum = 0
    csum = 0
    for i in player:
        psum += i
    for i in computer:
        csum += i
    
    print(f"Player hand: {player}")
    print(f"Computer Hand: {computer}")

    if not checkGameOver(player) and not checkGameOver(computer):
        if psum > csum:
            print("You Win")
        elif csum > psum:
            print("You Lose")
        else:
            print("Draw")
    elif checkGameOver(player):
        checkGameOver(player)
    else:
        checkGameOver(computer)



playing = input("Do you want to start(y/n): ")

while playing == 'y':
    
    print("Dealing Cards...")
    time.sleep(1)
    os.system('cls')
    deal()
    print("Cards has been dealt")
    print(f"You cards are {player}")
    print(f"One of the computer's cards is {computer[0]}")

    wantcard = input("Hit?(y/n): ")
    while wantcard == 'y':
        playerhit()
        if checkGameOver(player):
            break
        wantcard = input("Hit again(y/n): ")
    
    if checkGameOver(player):
        checkGameOver(player)
    else:
        computerhand()
        if not checkGameOver(computer):
            Winner()

    playing = input("Start another game(y/n): ")
    if playing == 'y':
        player.clear()
        computer.clear()
