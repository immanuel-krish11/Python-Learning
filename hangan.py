import random

word_list = ["camel", "mouse", "baboon"]

chosen_word = random.choice(word_list)
print(chosen_word)
placeholders = "_"*len(chosen_word)
print(placeholders)

game_over = False
correct_letters = []
lives = 6
while not game_over:
    guess = input("Guess a letter: ").lower()
    display=""
    for letter in chosen_word:
        if guess == letter:
            display+= letter
            correct_letters.append(letter)
        elif letter in correct_letters:
             display+=letter
        else:
            display+="_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"{lives}/6 lives remaining.")
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You Win")
