#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:07:58 2018

@author: jasleenarora
"""

# Read the values from intermediate file
with open('intermediate.txt','r') as f:
    content = f.readlines()
    
    
p = int(content[0])
g = int(content[1])
a = int(content[2])
c1 = int(content[3])
c2 = int(content[4])

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

# Converts binary to integer    
def bin2int(binary):
    return int(binary,2) # this tells the function that the input 'binary' is in base 2 and it converts it to base 10


# This will convert integer to character
def int2msg(integer):
    return bin2msg2(int2bin(integer))



# Write the conversion from binary to character in one line
def bin2msg2(binary):
    return ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))


def ElGamal(p,g,a,c1,c2):
    # Step1: calculate ((c1)^a)^p-2
    temp = fastPower(c1,a,p)
    s1 = fastPower(temp,p-2,p)
    
    # Step2: Multiply this by c2
    s2 = (s1*c2)%p
    
    # Step3: Convert this to character
    msg = int2msg(s2)
    print("The decoded message is: ",msg)
    
ElGamal(p,g,a,c1,c2)