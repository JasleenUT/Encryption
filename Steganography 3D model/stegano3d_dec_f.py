#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:56:37 2019

@author: jasleen
@task: Stegano Decrypt
"""
g = 7814

b = 327
A = 7980

# convert binary string into alpha-numeric message
def bin2msg(binary):
    return ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))
# convert alpha-numeric message into a binary string
def msg2bin(message):
    return ''.join(['{0:08b}'.format(ord(i)) for i in message])
# convert binary string into a traditional decimal number
def bin2int(binary):
    return int(binary,2)
# convert traditional number into binary string
def int2bin(integer):
    binString = ''
    while integer:
        if integer % 2 == 1:
            binString = '1' + binString
        else:
            binString = '0' + binString
        integer //= 2
    while len(binString)%8 != 0:
        binString = '0' + binString
    return binString
# using above functions, convert alpha-numeric message into a number
def msg2int(message):
    return bin2int(msg2bin(message))
# using above functions, convert a number into an alpha-numeric message
def int2msg(integer):
    return bin2msg(int2bin(integer))

def xorbit(binary,key):
    ciphertext = ''
    for i in range(len(binary)):
        ciphertext = ciphertext + str(int(binary[i])^int(key[i%len(key)]))
    return ciphertext

def fastPower(g,A,N):
    a=g
    b=1
    while A>0:
        if A%2 == 1:
            b = (b*a)%N
        a = (a*a)%N
        A = A//2
    return b

def get_gcode(filename):
    with open(filename, 'r') as f_gcode:
        data = f_gcode.read()
        return (data)

def find_length(line):
    # Search for semicolon i.e. '59595959'
    line1 = line.split(" ")
    if line1[1].startswith('X'):
        # Pick the X coordinate
        temp = line1[1]
        x = temp[-2:]
        
        # Pick the Y coordinate
        temp = line1[2]
        y = temp[-2:]
    else:
        # Starts with F
        
        # Pick the X coordinate
        temp = line1[2]
        x = temp[-2:]
        
        # Pick the Y coordinate
        temp = line1[3]
        y = temp[-2:]
    return (x,y)
            
def diffie_helman_dec(B,a,p,ciphertext):
    # Calculate the shared key
    key = fastPower(B,a,p)
    # Convert the key into binary
    key_binary = int2bin(key)
    # The input text is in integer, convert it to binary
    text_bin = int2bin(int(ciphertext))
    text_bin = str(text_bin)
    # XOR the key and the input
    xor=xorbit(text_bin,key_binary)
    # Convert the output to integer
    out_int = bin2int(xor)
    return out_int            
            
    
def stegano_dec(data):
    # Split it at newline
    values = []
    numbers = []
    f_values = []
    c=0
    i=0
    data_lines = data.splitlines()
    flag = True
    while flag:
        if ((data_lines[i].startswith('G1 X')) or (data_lines[i].startswith('G0 X')) or ((data_lines[i].startswith('G1 F')) and ('X' in data_lines[i])) or ((data_lines[i].startswith('G0 F')) and ('X' in data_lines[i]))):
            if (";" not in data_lines[i]):
                # Find the length of the message
                values = find_length(data_lines[i])
                temp = ''.join(values)
                numbers.append(temp)

        i+=1
        f_values = ''.join(numbers)

        if f_values.find('59595959')>=0:
            flag = False
        loc = f_values.find('59595959')
        length = f_values[0:loc]

    a = len(length)
    

    
    dec_data = []

    n = int(length) + 8 + a
    t = (8 + a)//4
    j=0

    n = n//2
    c=0

    flag = True
    i = 0
    while flag:
        if ((data_lines[i].startswith('G1 X')) or (data_lines[i].startswith('G0 X')) or ((data_lines[i].startswith('G1 F')) and ('X' in data_lines[i])) or ((data_lines[i].startswith('G0 F')) and ('X' in data_lines[i]))):
            if (";" not in data_lines[i]):

                values = find_length(data_lines[i])
                temp = ''.join(values)               
                dec_data.append(temp)
                c+=2
        if c >= n:
            flag = False                
        i+=1
    cond_dec_data = ''.join(dec_data)
    length_value = []
    
    # Get the length of the message
    for i in range(0,loc):
        length_value.append(cond_dec_data[i])
    length_value = ''.join(length_value)

    
    # Find the location of message start and message end
    msg_start = len(length_value) + 8

    msg_end = msg_start + int(length_value)

    
    dec_msg = []
    for i in range(msg_start,msg_end):
        dec_msg.append(cond_dec_data[i])
    dec_msg = ''.join(dec_msg)

        

    
    
    # decrypt it using diffie helman
    B = 10139
    a = 301
    p = 27077
    dec_int_dh = diffie_helman_dec(B,a,p,dec_msg)

    a = diffie_helman_dec(B,a,p,'1045092304294006805912749274091057174387289185699021584143196195178107936555703886342144087118090')

    
    
    # Convert this into character message
    print (int2msg(int(dec_int_dh)))
        
    
if __name__ == "__main__":
    # Get the encrypted data
    data = get_gcode("myOutFile1.gcode")
    stegano_dec(data)
    

