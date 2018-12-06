#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:09:24 2018

@author: Jasleen
"""

# Pillow library for Image processing
from PIL import Image
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from numpy import array



# One line function to convert characters to binary
def msg2bin2(message):
    return ''.join(['{0:08b}'.format(ord(i)) for i in message])

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

def divide_2(binary_message):
    n = 2
    input_g2 = [binary_message[i:i+n] for i in range(0, len(binary_message), n)]
    return(input_g2)
    
# Converts binary to integer    
def bin2int(binary):
    return int(binary,2)

def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def bin2msg(binary):
    return ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))
    

def steganography(image,message):
    size = image.size
    # Convert the image into pixels. This will give the RGB values of each pixel in the image in a list
    pix_val = array(image)
    
    # Convert the message to binary
    binary_message = msg2bin2(message)
    l = len(binary_message)
    
    # Convert the length to binary
    len_binary_message = int2bin(l) 
    
    # Check if the length is a multiple of 8 because it will be divided into parts of 8 during decryption
    str1 = ''
    v = len(len_binary_message)%8
    if(v != 0):
        temp = 8-v
        for i in range(0,temp):
            str1='0'+str1
        len_binary_message = str1 + len_binary_message
    
    
    # Check the length of the input message, if it is not a multiple of 2, then add a '0' at the end of the message
    if(len(binary_message)%2 != 0):
        binary_message = binary_message + '0'
    
    # APPROACH: FIRST, THE INPUT INITIALLY SHOULD BE THE LENGTH OF THE INPUT MESSAGE FOLLOWED BY A SEMICOLON
    # WHICH WILL TELL THAT THE MESSAGE IS STARTING NOW
    
    #APPEND IT BY A SEMICOLON
    semicolon = '00111011'
    binary_message = semicolon + binary_message
    
    # Combine the length of the binary message to the actual binary message to be appended in the image
    final_binary = len_binary_message + binary_message
    
    # Divide it into groups of 2
    final_binary_2 = divide_2(final_binary)
    
    #print("no of pixels that need to be replaced")
    lb = len(final_binary_2)

        
        
    # REPLACEMENT 
    t=0
    for i in range(10,size[0]):
        for j in range(0,size[1]):
            for k in range(0,3):
                if (t<lb):
                    temp = int2bin(pix_val[i][j][k])
                    a = final_binary_2[t]
                    temp = (temp[:-2])+a
                    
                    # Convert this back to integer
                    temp_i = bin2int(temp)
                    # replace it back
                    pix_val[i][j][k] = temp_i
                    t+=1
                    
    
                    
    # Convert the pixels back to the image                    
    img = Image.fromarray(pix_val)
    img.show()
    img.save("output_img.png")  
    print("Message has been encrypted. 'output_img.png' is the output image")

    
def stegano_dec(image):
    size = image.size
    pix_val = array(image)
            
    str_len = ''
            
            
    # Find the semicolon
    found = False
    str_temp = ''
    i, j, k = 10,0,0
    while (i < size[0]) and (not found):
        j = 0
        while (j < size[1]) and (not found):
            k = 0
            while (k < 3) and (not found):
                temp = int2bin(pix_val[i][j][k])
                last_two = temp[-2:]
                #Save it for the length extraction
                str_len = str_len + last_two
                str_temp = str_temp + last_two
                # if our string is longer than a byte, throw away the previous byte
                if (len(str_temp) > 8):
                    str_temp = str_temp[-2:]
                if(str_temp == '00111011'):
                    found = True
                    break
                k+=1
            if not found:
                j+=1
        if not found:
            i+=1
    # shift to the next pixel
    if(k<3):
        k+=1
    elif(j<size[1]):
        j+=1
    else:
        i+=1

    
    len_message = str_len[:-8]
    len_message_int = bin2int(len_message)

    
    # Extract the message
    # No of bytes that have been replaced is (len_message_int)/2
    len_message_dec = int(len_message_int/2)
    count = 0
    str_dec = ''
    
    for a in range(i,size[0]):
        for b in range(j,size[1]):
            while (k<3) and (count < len_message_dec):
                temp = int2bin(pix_val[a][b][k])
                last_two = temp[-2:]
                str_dec = str_dec + last_two
                k+=1
                count+=1
            k=0
            
    str_dec = str(str_dec)
    out_str = bin2msg(str_dec)
    
    print("The decrypted message is: ",out_str)
                
    
    
if __name__ == "__main__":
    print("Welcome to Steganography")
    n = input("1. Encode\n2. Decode\n")
    if (n == '1'):
        image_enc = input("Enter the name of the image:\n")
        image = Image.open(image_enc)
        message = input("Enter the message to be encrypted:\n")
        steganography(image,message)
    if (n == '2'):
        image_dec = input("Enter the name of the image:\n")
        image = Image.open(image_dec)
        stegano_dec(image)

    
