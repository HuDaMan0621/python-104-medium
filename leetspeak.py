# 1. "leetspeak"

# Given a paragraph of text as a String, print the paragraph in leetspeak. It's a "clever" way to sound like a "hacker".

# (See https://en.wikipedia.org/wiki/Leet for more information.)

# To translate a String to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

# A -> 4
# E -> 3
# G -> 6
# I -> 1
# O -> 0
# S -> 5
# T -> 7

# Example: If your program is given the String 
# "I am a leet programmer", it should print "1 4m 4 l337 pr0gr4mm3r" 
# as the leetspeak translation
word = input('user input ')
for index in range(len(word)):
    letter = word[index]
    #print (f'{letter}')
    if letter == 'A':
        print ('4') 
    elif letter == 'E':
        print ('3')    
    elif letter == 'G':
        print ('6')
    elif letter == 'I':
        print ('1')
    elif letter == 'O':
        print ('0')
    elif letter == 'S':
        print ('5')
    elif letter == 'T':
        print ('7')
        #E, G, I, O, S, T

# word = 'HELLO'for index in range(len(word)):    
# letter = word[index]    
# print(f'The letter {letter} is at index {index}')#The letter H is at index 0#The letter E is at index 1
# #The letter L is at index 2
# #The letter L is at index 3
# #The letter O is at index 4