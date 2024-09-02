import word_levels
import random

#level  chose, dashes print, user input, on correct it places that character at the  right index
#in case of wrong it says wrong guess chances reduce and if finished game over 
def hangman():
    level = input("Choose level 1. Easy  2. Medium  3. Hard: ").lower()

    if level == "easy":
        generated = random.choice(word_levels.Easy)
    elif level == "medium":
        generated = random.choice(word_levels.medium)
    else:
        generated = random.choice(word_levels.hard)

    dashes = ["_"]*len(generated)
    print(" ".join(dashes))
    
    chances=3

    while "_" in dashes and chances !=0:
        user_input = input("Guess the character: ").lower()
        
        if user_input in generated:
            for i in range(len(generated)):
                if generated[i] == user_input:
                    dashes[i] = user_input
            print(" ".join(dashes))
        else:
            chances -= 1
            print(f"Wrong guess, You have {chances} chances left")

    if "_" not in dashes:
        print("Congratulations! You've guessed the word:", generated)
    else:
        print(f"Sorry, you've run out of chances. The word was: {generated}")


def play_again():
    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again == "y":
            hangman()
        elif play_again == "n":
            print("Thanks for playing! We hope to see you soon.")
            break
        else:
            print("Invalid input. Enter y to play again and n to stop.")

hangman()
play_again()