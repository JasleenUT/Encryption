#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:16:57 2018

@author: jasleenarora
"""

with open('DHExtraInput.txt','r') as f:
    lines = f.readlines()
p = int(lines[0])
g = int(lines[1])
b = int(lines[2])
A = int(lines[3])
text = lines[4]
text = int(text.strip())
text = str(text)


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
        print("This is plaintext")
        return 1
    else:
        print("This is ciphertext")
        return 0
    
# Finding the inverse
# g is the number, N is modulus and A is N-2
def fastPower(g,A,N):
    a=g
    b=1
    while A>0:
        if A%2 == 1:
            b = (b*a)%N
        a = (a*a)%N
        A = A//2
    return b
    
# This script converts an integer to binary
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

    
def decrypt(p,g,b,A,text):
    print("The decrypted ciphertext is:")
    # 1. Convert the binary to decimal
    integer_text = bin2int(text)
    
    # 2. Calculate the shared key
    key = fastPower(A,b,p)
    
    # 3. Find the inverse of shared key mod p
    key_inverse = fastPower(key,p-2,p)
    
    # 4. Multiply the ciphertext with the shared key mod(p)
    product = (integer_text*key_inverse)%p
    
    # 5. Convert this to binary
    text_bin = int2bin(product)
    
    # 6. Convert to character
    plaintext = bin2char(text_bin)
    print(plaintext)
    

    
def encrypt(p,g,b,A,text):

    print("The encrypted plaintext is:")
    # 1. Convert the binary plaintext into decimal
    bin_text = bin2int(text)
    
    # 2. Calculate the shared key mod p 
    key = fastPower(A,b,p)
    
    # 3. Multiply the input with shared key
    product = (bin_text*key)%p
    
    # 4. Convert the product to binary
    text_bin = int2bin(product)
    print(text_bin)

# Converts binary to integer    
def bin2int(binary):
    return int(binary,2) # this tells the function that the input 'binary' is in base 2 and it converts it to base 10
    
    
def diffie_hellman(text):
    # Step1: Convert the input text from binary to characters
    characters = bin2char(text)
    # Step2: Check whether the input is plaintext or ciphertext
    # If it is plaintext, encrypt it. If it is ciphertext, decrypt it
    temp = check_text(characters)
    if(temp == 0):
        decrypt(p,g,b,A,text)
    else:
        encrypt(p,g,b,A,text)
        
    
diffie_hellman(text)
    