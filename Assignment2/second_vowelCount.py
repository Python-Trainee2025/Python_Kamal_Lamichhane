# 2. Accept a word/sentence from the user and count how many vowels (a, e, i, o, u) are present in it.

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
sentence = input("Enter a sentence: ")

count = 0
for char in sentence:
    if char in vowels:
        count += 1

print(f'Number of vowels: {count}')