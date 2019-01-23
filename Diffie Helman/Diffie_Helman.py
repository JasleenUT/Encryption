#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:56:04 2018

@author: jasleenarora
"""

# This script will perform diffie hellman encryption/decryption

# Get the values of p,g,A and my private key, b is 327


with open('DHInput.txt','r') as f:
    lines = f.readlines()
p = int(lines[0])
print("p",p)

g = int(lines[1])
print("g",g)
b = int(lines[2])
A = int(lines[3])
text = lines[4]

# Open and input the dictionary
dictionary = open('dictionary.txt','r')
words = []
#separate words by line and append them to dictionary
for word in dictionary.read().split('\n'):
    words.append(word)
dictionary.close()


# Fast powering Algorithm
# g=base, A=power, N=modulus
def fastPower(g,A,N):
    a=g
    b=1
    while A>0:
        if A%2 == 1:
            b = (b*a)%N
        a = (a*a)%N
        A = A//2
    return b


# This function converts an integer to binary
def int2bin(integer):
    if integer == 0:
        return('00000000')
    binString = ''
    while integer:
        if integer % 2 == 1:
            binString = '1' + binString
        else:
            binString = '0' + binString
        integer //=2
        
    while len(binString)%8 != 0:
        binString = '0' + binString
    return binString
    
# This will XOR 2 binary numbers
def xorbit(binary,key):
    ciphertext = ''
    for i in range(len(binary)):
        ciphertext = ciphertext + str(int(binary[i])^int(key[i%len(key)]))
    return ciphertext

# This will convert binary to character
def bin2char(binary):
    # split binary input into groups of 8
    n=8
    output = [binary[i:i+n] for i in range(0, len(binary), n)]
    char = []

    for i in range(0,len(output)):
        char.append(chr(int(output[i],2)))
    char = ''.join(char)
    return(char)
    
# Check whether it is plaintext or ciphertext
def check_text(characters):
    # Split the message into words
    message_word = characters.split(' ')
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
        # Plaintext
        return 1
    else:
        # Ciphertext
        return 0
        
   
# Diffie Hellman Cryptography
def diffie_hellman(A,b,p,text):
    # Calculate the key
    key = fastPower(A,b,p)
        
    # Convert the key into binary
    key_binary = int2bin(key)
    # To remove this error
    # invalid literal for int() with base 10: '\n'
    text = int(text.strip())  
    print(type(text))
    text = str(text)
    
    # XOR the key and the input
    xor=xorbit(text,key_binary)
    # Convert binary to characters
    characters = bin2char(xor)
    characters = characters.upper()
    # Check whether it is plaintext or ciphertext
    temp = check_text(characters)
    if(temp == 0):
        print("The input was plaintext, it has been converted to ciphertext")
        print(xor)
    if(temp == 1):
        print("The input was ciphertext, it has been converted to plaintext")
        print(characters)
      
    
diffie_hellman(A,b,p,text)


    
    