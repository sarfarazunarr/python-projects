import random

words = ['NATURE', 'NATIONAL', 'WORLD', 'PAKISTAN', 'INDIA', 'LAPTOP', 'LIFE']
word = random.choice(words)

total_chances = 7

guess_word = '_'*len(word)

while total_chances != 0:
    print(guess_word)
    letter = input('Guess a letter: ').upper()
    if letter in word:
        for index in range(len(word)):
            if(word[index]==letter):
                guess_word = guess_word[:index]+letter+guess_word[index+1:]
        if(guess_word == word):
            print('Great Bro! You Win🤗')
            break
    else:
        total_chances -= 1
        print('Oh Failed')
        print('Remaining chances', total_chances)
else:
    print('Game Over')
    print('You Lose')
    print('All the chances are exhausted')
    print('The Correct word is', word)

