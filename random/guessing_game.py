# Create a guessing game with user input

secret_word = 'python'
guess_limit = 3
attempt = 0
word = input('Enter word: ')

while attempt < guess_limit:
    attempt =+ 1
    if word != secret_word:
        print('Invalid answer, Try again!')
    elif word == secret_word:
        print('You won the game')
    else:
        print('You\'re out of attempts!')

print('Done')