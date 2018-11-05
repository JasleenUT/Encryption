#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 15:37:01 2018

@author: jasleenarora
"""

# define our alphabet and create a list of both upper and lower case to handle it in the message
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
caps = list(alphabet)
lower = list(alphabet.lower())

# Open the message from the input file
message = open('input.txt','r')

#read lines and append to string
line1 = ''
for newline in message.readlines():
    line1 = line1 + str(newline)
print("The encrypted text: ")
print(line1)
    
# close the opened file
message.close()
    
# Convert the input string into a list
letters = list(line1)

dictionary = open('dictionary.txt','r')
words = []
#separate words by line and append them to dictionary
for word in dictionary.read().split('\n'):
    words.append(word)
dictionary.close()

# For the decryption function, the steps are as follows:
# 1. Loop through all the possible 26 keys
# 2. Subtract each key from each letter
# 3. Combine to form words
# 4. Parse each word through the dictionary and find whether the word is in the dictionary or not
# 5. Calculate the ratio, I have taken alpha as 0.2. If it is more than 0.2, then I have taken it as decrypted plaintext

def decrypt(line1):
    letters_d = list(line1)
    for key in range(0,26):
        dec = []
        for letter in line1:
            if letter in lower:
                num = lower.index(letter)
                num = num - key
                num = num%26
                letter = lower[num]
            elif letter in caps:
                num = caps.index(letter)
                num = num - key
                num = num%26
                letter = caps[num]
            dec.append(letter)
        text = ''.join(dec)
        text = text.upper()
        temp = text.split(' ')
        y=0
        n=0
        for t in temp:
            if t in words:
                y+=1
            else:
                n+=1

        if(n==0):
            n=0.1
            
        d = y/n
        if(d>0.2):
            temp = ' '.join(temp)
            print("This is the decrypted text: ")
            print(temp)
            f = open('output.txt','w')
            f.write(temp)
        
# Call the function    
decrypt(line1)
