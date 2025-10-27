# Get input from user and check if it is palindrome

word = input('Enter a word: ')

if word.upper() == word[::-1].upper():
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')
