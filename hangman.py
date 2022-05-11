#Hang Man project
#to generate a word list I used randomlists.com
import random
from ASCII_Art import HangMan
from ASCII_Art import logo
from Word_List import word_list

print(logo)
chosen_word = random.choice(word_list) #here I randomly choose one word from the list
Blanks = ["_"]*len(chosen_word) #here I create a list with the length of the chosen word

print(f"(As a hint!)Your word is: {chosen_word}") #testing if input letter is in this word and what is the output
print(Blanks)

End_of_the_Game = False
life = 6

while not End_of_the_Game:
    # Here user insert a letter
    guess = input("What is the letter?: \n")
    #here we search if letter is in chosen word and swap underscore with this letter
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            Blanks[pos] = letter

    if guess not in chosen_word:
        life -= 1
        print(f"Your life is: {life}")
        if life == 0:
            End_of_the_Game = True
            print("You lose. ;C")

    print(HangMan[life])
    print(Blanks)

    if "_" not in Blanks: #we check if underscore is no more in Blanks and then we change End_of_the_Game to true and loop ends
        End_of_the_Game = True
        print("Yay! You win!")
