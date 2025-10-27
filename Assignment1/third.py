# Input a sentence or a paragraph from user
# and extract how many unique words are used and display the count

para = input('Enter anything: ').replace(".", "").split(" ")

unique_words = set(para)

print("Number of unique words: ", len(unique_words))