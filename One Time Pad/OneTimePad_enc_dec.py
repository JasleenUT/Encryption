#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 15:06:30 2018

@author: jasleenarora
"""

# Create an alphabet list
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
caps = list(alphabet)

# Open and input the dictionary
dictionary = open('dictionary.txt','r')
words = []
#separate words by line and append them to dictionary
for word in dictionary.read().split('\n'):
    words.append(word)
dictionary.close()

# Open the message from the input.txt file
with open('input.txt','r') as f:
    content = f.read().splitlines()
    
# the first line is the key
key = content[0]
num_k = key.split(' ')
num_k = list(map(int, num_k))
print(num_k)

# the second line is the message
message = content[1]

# I have decided to work in upper case, so I am converting the message to uppercase
message = message.upper()
# Split the message into words
message_word = message.split(' ')

# Define the encryption function
enc = []
def oneTimePad_encrypt(message):
    count = 0
    # Convert the message into list of characters
    letters = list(message)
    # 1. Find the index of every character in letters
    # 2. Add it to the number from the key list
    # 3. Increment the counter of the key list so that the next character is added to the next number in the key list
    # 4. Find the modulus
    # 5. Convert it back to the character
    for letter in letters:
        if letter in caps:
            num = caps.index(letter)
            num = num + num_k[count]
            count = count+1
            num = num%26
            letter = caps[num]
        enc.append(letter)
    # Join the ciphered characters to form the ciphertext
    text = ''.join(enc)
    print(text)
    f = open('encryption.txt','w')
    f.write(text)
    
# Define the decryption function  
dec = []
def oneTimePad_decrypt(message):
    count = 0
    # Convert the message into list of characters
    letters = list(message)
    # 1. Find the index of every character in letters
    # 2. Subtract it from the number from the key list
    # 3. Increment the counter of the key list so that the next character is added to the next number in the key list
    # 4. Find the modulus
    # 5. Convert it back to the character
    for letter in letters:
        if letter in caps:
            num = caps.index(letter)
            num = num - num_k[count]
            count = count+1
            num = num%26
            letter = caps[num]
        dec.append(letter)
    # Join the deciphered text to produce a plaintext
    text = ''.join(dec)
    print(text)
    f = open('decryption.txt','w')
    f.write(text)




# Now pass each word through the dictionary to see that whether the message is plaintext or ciphertext
y=0
n=0
for m in message_word:
    if m in words:
        y+=1
    else:
        n+=1
# To handle division by zero
if(n == 0):
    n=0.1
        
d = y/n

if(d>0.2):
    print("This is plaintext")
    # Since this is plaintext, call the function to encrypt it
    oneTimePad_encrypt(message)
else:
    print("This is ciphertext")
    # Since this is the ciphertext, call the function to decrypt it
    oneTimePad_decrypt(message)
    

    
    
    
    
    
    