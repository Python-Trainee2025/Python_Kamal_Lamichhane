# Take input from user for two words, and check if they are anagrams
# (anagram example: listen and silent -> both contain the same number and set of alphabets)

words = input("Enter two words separated by space: ").split(" ")

sorted_first = sorted(words[0])
sorted_second = sorted(words[1])

if sorted_first == sorted_second:
    print(f'{words[0]} and {words[1]} are anagrams')
else:
    print(f'{words[0]} and {words[1]} are not anagrams')