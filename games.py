import random

def scissors_paper_stone():
    print("Welcome to Scissors-Paper-Stone! Let us start playing")
    while True:
        user_choice = str(input("Enter your choice: "))
        user_choice = user_choice.lower()
        if user_choice == 'quit':
            break

        if user_choice in ["scissors","paper","stone"]:
            computer_choice = random.choice(["scissors","paper","stone"])
            print(f"I picked {computer_choice}")
            if user_choice == computer_choice:
                print("It's a draw!")
            elif user_choice == "scissors":
                if computer_choice == "paper":
                    print("You win!")
                else:
                    print("You lose!")
            elif user_choice == "paper":
                if computer_choice == "stone":
                    print("You win!")
                else:
                    print("You lose!")
            elif user_choice == "stone":
                if computer_choice == "scissors":
                    print("You win!")
                else:
                    print("You lose!")
        else:
            print("enter a valid option and ensure there are no spelling mistakes!: ")
            continue

def hangman():
    print("Welcome to Hangman! Let us start playing")
    list_of_words = ["apple","banana","orange","mango","pineapple","watermelon","grapes","strawberry","blueberry","cherry","papaya","pear","peach","plum","apricot","avocado","blackberry","raspberry","cantaloupe","fig","grapefruit","guava","honeydew","kiwi","lemon","lime","lychee","nectarine","olive","pomegranate","tomato"]
    #hangman program in which the user has to guess the word by guessing the letters and at the end of game the user is given the option to play again or not
    #if user enters N or n then the program ends
    #if user enters Y or y then the program restarts
    #if user enters anything else then the program asks the user to enter a valid option
    while True:
        word = random.choice(list_of_words)
        word = word.lower()
        word_letters = set(word)
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        used_letters = set()
        lives = 6
        while len(word_letters) > 0 and lives > 0:
            print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print("Current word: ", " ".join(word_list))
            user_letter = input("Guess a letter: ").lower()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives = lives - 1
                    print("Letter is not in word.")
            elif user_letter in used_letters:
                print("You have already used that character. Please try again.")
            else:
                print("Invalid character. Please try again.")
        if lives == 0:
            print("You died, sorry. The word was", word)
        else:
            print("You guessed the word", word, "!!")
        print("Do you want to play again? (Y/N)")
        play_again = input()
        if play_again == "n" or play_again == "N":
            break
        elif play_again == "y" or play_again == "Y":
            continue
        else:
            print("Enter a valid option")
            continue