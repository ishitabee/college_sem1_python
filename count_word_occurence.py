#Saranya is working on a text analysis tool to help writers quickly count the occurrences of specific words in their drafts. She needs a program that can efficiently count how many times a word appears, regardless of whether it's uppercase or lowercase. 

# Taking user input for the line in which the word occurrence needs to be counted.
line=input().lower()   

# Taking user input for the word whose occurrence needs to be counted.
word=input().lower()

# Counting the occurrences of the word in the line and storing it as result
result=line.count(word)
print(result)