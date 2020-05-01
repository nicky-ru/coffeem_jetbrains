line = input()
vowels = 'aeiou'

for letter in line:
    if letter.isalpha():
        if letter in vowels:
            print('vowel')
        else:
            print('consonant')
    else:
        break
