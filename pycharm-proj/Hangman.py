import random

attempted = 0
guessed_word = []
attempt_remaining = 5
wrong_guess = []
game_on = True
wrong = 0

name = input("Enter your name to start the game!!!!!!!!!! ")
print("Hello " + name + ", Welcome to the game! ")
word_list = ["hello", "apple", "banana", "guava", "litchi", "pineapple", "grapes"]
word = random.choice(word_list)
# print(word)
word_len = len(word)
# print("Length of the word is = {} " .format(word_len))
board_word = "_" * word_len
print(board_word)


def play_game():
    global board_word
    global game_on

    while game_on:

        if "_" in board_word:
            word_generate()

        else:
            print("your answer is complete ")
            game_on = False

    print("Your word is ", word)


def word_generate():
    global attempted
    global attempt_remaining
    global board_word
    global guessed_word
    global wrong
    global game_on

    # print("board has place ................... ")
    letter = input("Enter your guess to put in the word : ")

    if letter in guessed_word:
        print("Already guessed......... Try again")

    elif letter in word:
        # print("Gussed correct.......... ")
        attempted += 1
        guessed_word.append(letter)
        # attempt_remaining -= 1
        # print("Attempted ", attempted)
        print("Guessed = ", guessed_word)
        print("Remaining Attempt = ", attempt_remaining)

        for index, char in enumerate(word):
            if word[index] == letter:
                loc_letter = index
                # print("Index of {} in word " .format(letter), loc_letter)
                board_word = board_word[:loc_letter] + letter + board_word[loc_letter + 1:]
                print(board_word)

    else:
        print("your guessed letter is wrong and not fit in word")
        attempted += 1
        guessed_word.append(letter)
        attempt_remaining -= 1
        wrong_guess.append(letter)
        wrong += 1
        # print("Attempted ", attempted)
        print("Guessed = ", guessed_word)
        print("Remaining Attempt = ", attempt_remaining)
        # print("Wrong guessed", wrong_guess)
        if wrong == 1:
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif wrong == 2:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif wrong == 3:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif wrong == 4:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif wrong == 5:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            game_on = False
            print("Your attempt is over........... you lose the game")


play_game()