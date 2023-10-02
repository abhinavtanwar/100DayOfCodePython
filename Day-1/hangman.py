import hangmanAsciiArt as hmaa
import hangmanWords as hmw
import os

word = (hmw.giveWords()).lower()
lifes = 7
count = 0
guessed = ""
for i in range(0, len(word)):
    guessed += "_"

newguessed = list(guessed)

#print(word)
print(guessed)


while lifes>0:
    print(f"\nYou have {lifes} lifes left.")
    guess = input("\nGuess a letter: ")
    os.system('cls')
    
    if guess in guessed:
        print(guessed)
        print(hmaa.hangman[7-lifes])
        continue
    elif guess in word:
        for i in range(0, len(word)):
            if word[i] == guess:
                count += 1
                newguessed[i] = word[i]
        
        guessed = ''.join(newguessed)
        print(guessed)
        print(hmaa.hangman[7-lifes])
    else:
        print(guessed)
        print(hmaa.hangman[7-lifes])
        lifes = lifes - 1
    
    if count == len(word):
        print("\nYOU WIN MA")
        break

if lifes<=0:
    print("YOU LOSE")
    choice = input("Do you want to know the word(y/n): ")
    if choice == 'y':
        print(word)