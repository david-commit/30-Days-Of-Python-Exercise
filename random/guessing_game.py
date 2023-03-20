# Create a guessing game with user input

secret_word = 'python'
guess_limit = 3
attempt = 0
word = ''

while attempt < guess_limit:
    word = input('Guess word: ')
    if word != secret_word:
        print('Incorrect. Try again!')
        attempt += 1
    elif word == secret_word:
        print('You won the game!')
        break

if attempt == 3:
    print('You\'re out of attempts. You lose! ')