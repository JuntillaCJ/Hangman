import random
import stages

word_list = ["apple", "banana", "cherry", "chico", "durian", "lemon", "lychee", "mango", "melon"]
chosen_word = word_list[random.randint(0, len(word_list) - 1)]

display = []
display_string = ""
for letter in chosen_word:
    display.append("_")
    display_string += "_"
    display_string += " "

lives = 6
letterUsed = ""

print(stages.stages[lives])
print(f"{display_string} Lives: {lives}/6")

running = True
while running:

    guess = input("Enter a letter: ").lower()

    if guess in letterUsed:
        print(f"You already guessed {guess}.")
        continue
    else:
        letterUsed += guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    else:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = chosen_word[i]

    display_string = ""
    for char in display:
        display_string += char
        display_string += " "

    print(stages.stages[lives])
    print(f"{display_string} Lives: {lives}/6")

    if lives == 0:
        print(f"It was {chosen_word}. You lose. Better luck next time.")
        running = False

    if "_" not in display:
        print("You won!")
        running = False
