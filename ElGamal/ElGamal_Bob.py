#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:04:58 2018

@author: jasleenarora
"""

import random

# Read the values from input file
with open('ElGamalInput.txt','r') as f:
    content = f.readlines()

p = int(content[0])
g = int(content[1])
A = int(content[2])
a = int(content[3])

message = "HI"


###fast powered
def fastPower(g, A, N):
    a=g
    b=1
    while A>0:
        if A%2==1:
            b=(b*a)%N
            
        a=(a*a)%N
        A=A//2
        
    return b

# One line function to convert characters to binary
def msg2bin2(message):
    return ''.join(['{0:08b}'.format(ord(i)) for i in message])

# Converts binary to integer    
def bin2int(binary):
    return int(binary,2) # this tells the function that the input 'binary' is in base 2 and it converts it to base 10


# Function to convert character to integer
def msg2int(message):
    return bin2int(msg2bin2(message))


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


# Generate random number
def random_number():
    return(random.randint(10,101))
    
def ElGamal(message):
    # Convert input message to integer
    message_int = msg2int(message)
    print(message_int)
    
    # Generate random number
    r = random_number()
    
    # Calculate C1
    c1 = fastPower(g,r,p)
    print("c1 ",c1)
    
    # Calculate C2
    temp = fastPower(A,r,p)
    print(temp)
    c2 = (message_int*temp)%p
    print("c2 ",c2)

    
    # Write values to file
    with open('intermediate.txt','w') as out:
        out.write('{}\n{}\n{}\n{}\n{}\n'.format(p,g,a,c1,c2))
    
    
    
ElGamal(message)
    






