'''
Created on May 2, 2014

@author: ROCKSTAR
Script to check String operation
'''
pyg = 'ay'
original = input("Enter a word: ")
if len(original) > 0 and original.isalpha():
    print(original)
else:
    print ("empty string")
word=original.lower()
wl=len(word)
first=word[0]
print(first)
print(word[1:len(word)])
new_word=word[1:len(word)]+first+pyg
print(new_word)