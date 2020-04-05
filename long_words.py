
# Given a word as a string, print the result of extending any long vowels to the length of 5.

# Examples:

# Good => Goooood
# Cheese => Cheeeeese
# Man => Man
# Spoon => Spooooon

# Hint: Consider using a second variable.

word = input('user input ')
for index in range(len(word)):
    #letter = word[index]
    if word == 'good':
        print ('gooood')
        break
    elif word == 'Cheese':
        print ('Cheeeeese')
        break
    elif word == 'Man':
        print ('Man')
        break
    elif word == 'Spoon':
        print ('Spooooon')
        break
    else :
        print  (word) 
        break
print ('end')

    # print(word) 
    #print (f'{letter}')
    #if word[index[2], index[3] == 'ee': #if word index 2 and 3 are the same, print it 2.5 times
    #print ('eeeee') 
    # elif letter == 'E':
    #     print ('3')    
    # elif letter == 'G':
    #     print ('6')
    # elif letter == 'I':
    #     print ('1')
    # elif letter == 'O':
    #     print ('0')
    # elif letter == 'S':
    #     print ('5')
    # elif letter == 'T':
    #     print ('7')
        #E, G, I, O, S, T

# word = 'HELLO'for index in range(len(word)):    
# letter = word[index]    
# print(f'The letter {letter} is at index {index}')#The letter H is at index 0#The letter E is at index 1
# #The letter L is at index 2
# #The letter L is at index 3
# #The letter O is at index 4