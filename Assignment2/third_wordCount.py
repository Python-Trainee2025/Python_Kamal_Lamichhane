# 3. Read a text file and count the number of words in it.
# Handle the case where the file might not exist.

def fileWordCount(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.read().split(" ")
            return len(content)

    except FileNotFoundError as e:
        print("File not found")
        print(e)

print(f'Total words in the given file is {fileWordCount("MyFile.txt")}')