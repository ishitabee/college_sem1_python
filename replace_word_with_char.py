#Jin is working on a string manipulation problem. He needs to replace all occurrences of a specified pattern within a given word with a specified character. Write a program to help Jin achieve this task efficiently.

#user input for the pattern, word to be replaced, and the special character
pattern=input("Enter the pattern to be replaced: ")

word=input("Enter the word in the pattern that you would like replaced: ")

special_char=input("Enter the character you want to replace the word with: ")

#Replacing the pattern in the word with the special character
result=pattern.replace(word,special_char)

print(result)
