#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:55:46 2019

@author: jasleen
"""



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
    
# A is Alice public key that is used to encrypt the message
# p, g are public numbers
# b is the secret key of Bob
# text is the plaintext to be encrypted in integer format
def diffie_helman_enc(A,b,p,plaintext):
    # Calculate shared key
    key = fastPower(A,b,p)
    
    # Convert the key into binary
    key_binary = int2bin(key)
    
    # The input text is in integer, convert it to binary
    text_bin = int2bin(int(plaintext))
    
    # invalid literal for int() with base 10: '\n'
    text_bin = str(text_bin)
    
    # XOR the key and the input
    xor=xorbit(text_bin,key_binary)
    
    # Convert the output to integer
    out_int = bin2int(xor)
    return out_int
    
def preprocess_msg(message):
    # Convert message into integer
    msg_int = msg2int(message)
    g = 7814
    p = 27077
    b = 327
    A = 7980
    B = 10139
    a = 301
    
    # Encrypt the message with diffie helman
    msg_int_enc = diffie_helman_enc(A,b,p,msg_int)
    #print ("encrypted message ",msg_int_enc)
    #print ("length of enc msg: ",len(str(msg_int_enc)))
    
    # Pad the message if it is not a multiple of 2
    if (len(str(msg_int_enc)))%2 != 0:
        msg_int_enc = '0' + str(msg_int_enc)
    # Calculate length
    msg_len = len(str(msg_int_enc))
    #print ("msg_len ",msg_len)
    # pad it to make multiple of 2

    if (len(str(msg_len)))%2 != 0:
        msg_len = '0' + str(msg_len)

        
            
    semicolon = '59595959'
    

    
    # Final message = length of message + semicolon + message
    final_msg = str(msg_len) + semicolon + str(msg_int_enc)  


    return final_msg

def encrypt(line,c1,c2):
    line1 = line.split(" ")
    if line1[1].startswith('X'):
########################################################################################### example replacement code
#####################################################################################################################
#####################################################################################################################
        # Make a change in th X parameter
        temp = line1[1].split(".")
        #print (temp)
        temp[1] = temp[1] + c1
        #print (temp)
        '''
        if len(temp)==1:            ########################################## it is infrequent, but sometimes the coordinates are whole numbers with no decimals, this accounts for that
            temp.append('')         #####################################################################################################################################################
        if len(temp[1])>=2:
            temp[1] = temp[1]+c1
        else:
            temp[1] = temp[1]+'00'+c1
            '''
        temp = ".".join(temp)
        # Replace
        line1[1] = temp
        
        # Make a change in the Y parameter
        temp = line1[2].split(".")
        temp[1] = temp[1] + c2
        #print (temp)
        '''
        if len(temp)==1:            ########################################## it is infrequent, but sometimes the coordinates are whole numbers with no decimals, this accounts for that
            temp.append('')         #####################################################################################################################################################
        if len(temp[1]) >=2:
            temp[1] = temp[1]+c2
        else:
            temp[1] = temp[1]+'00'+c2
            '''
        temp = ".".join(temp)

        # Replace
        line1[2] = temp
        line1 = ' '.join(line1)
################################################################################################################
################################################################################################################
############################################################################################### end example code

        
    else:
        # Make changes to the X parameter
        temp = line1[2].split(".")
        #print (temp)
        temp[1] = temp[1] + c1
        #print (temp)
        '''
        if len(temp)==1:
            temp.append('')
        if len(temp[1])>=2:
            temp[1] = temp[1]+c1
        else:
            temp[1] = temp[1]+'00'+c1
            '''
        temp = ".".join(temp)
        # Replace
        line1[2] = temp
        
        # Make a change in the Y parameter
        temp = line1[3].split(".")
        #print (temp)
        temp[1] = temp[1] + c2
        #print (temp)
        '''
        if len(temp)==1:            ########################################## it is infrequent, but sometimes the coordinates are whole numbers with no decimals, this accounts for that
            temp.append('')         #####################################################################################################################################################
        if len(temp[1]) >=2:
            temp[1] = temp[1]+c2
        else:
            temp[1] = temp[1]+'00'+c2
            '''
        temp = ".".join(temp)
        
        
        # Replace
        line1[3] = temp
        line1 = ' '.join(line1)

        
    return line1

        
    
def stegano_encrypt(data,message):
    msg = preprocess_msg(message)

    # Split the message into groups of 2
    n=2
    msg_split = [(msg[i:i+n]) for i in range(0, len(msg), n)]


    # Length of message split, i.e. number of replacements
    lms = len(msg_split)
    
    if lms%2 != 0:
        msg_split.append('00')
        #msg_split.insert(0,'00')
    lms = len(msg_split)
        

    
    # Split data at newline
    data_lines = data.splitlines()
    #print (data_lines[1])
    #print ("Before")
    #print(data_lines)

    ############################################################ example while loop here
    ####################################################################################
    # Get the data from the gcode than has to be encrypted  ############################
    count = 0                                               ############################
    i = 0                                                   ############################
    flag = True                                             ############################
    while flag:                                             ############################
        if ((data_lines[i].startswith('G1 X')) or (data_lines[i].startswith('G0 X')) or ((data_lines[i].startswith('G1 F')) and ('X' in data_lines[i])) or ((data_lines[i].startswith('G0 F')) and ('X' in data_lines[i]))):
            if (";" not in data_lines[i]):                  ############################
                data_lines[i] = encrypt(data_lines[i],msg_split[count],msg_split[count+1])
                count = count+2                             ############################
        if count >= lms:                                    ############################
            flag = False                                    ############################
        i += 1                                              ############################
    ####################################################################################
    ####################################################################################
        #print ('check5')
    #print (type(data_lines))
    #data_out = ''.join(data_lines)
    return data_lines

        
        
    
    
    
if __name__ == "__main__":
    # Get data from gcode file
    data = get_gcode('LTAZ6_helmet.gcode')
    # long message
    '''
    message = "THE MOON BLEW UP WITHOUT WARNING AND FOR NO APPARENT reason. It was waxing, only one day short of full. The time was 05:03:12 UTC. Later it would be designated A+0.0.0, or simply Zero. An amateur astronomer in Utah was the first person on Earth to realize that something unusual was happening. Moments earlier, he had noticed a blur flourishing in the vicinity of the Reiner Gamma formation, near the moon’s equator. He assumed it was a dust cloud thrown up by a meteor strike. He pulled out his phone and blogged the event, moving his stiff thumbs (for he was high on a mountain and the air was as cold as it was clear) as fast as he could to secure the claim to himself. Other astronomers would soon be pointing their telescopes at the same dust cloud—might be doing it already! But—supposing he could move his thumbs fast enough—he would be the first to point it out. The fame would be his; if the meteorite left behind a visible crater, perhaps it would even bear his name. His name was forgotten. By the time he had gotten his phone out of his pocket, his crater no longer existed. Nor did the moon."
    
    When he pocketed his phone and put his eye back to the eyepiece of his telescope, he let out a curse, since all he saw was a tawny blur. He must have knocked the telescope out of focus. He began to twiddle the focus knob. This didn’t help. \
    Finally he pulled back from the telescope and looked with his naked eyes at the place where the moon was supposed to be. In that moment he ceased to be a scientist, with privileged information, and became no different from millions of other people around the Americas, gaping in awe and astonishment at the most extraordinary thing that humans had ever seen in the sky.\
    In movies, when a planet blows up, it turns into a fireball and ceases to exist. This is not what happened to the moon. The Agent (as people came to call the mysterious force that did it) released a very large amount of energy, to be sure, but not nearly enough to turn all the moon’s substance into fire.\
    The most generally accepted theory was that the puff of dust observed by the Utah astronomer was caused by an impact. That the Agent, in other words, came from outside the moon, pierced its surface, burrowed deep into its center, and then released its energy. Or that it simply kept on going out the other side, depositing enough energy en route to break up the moon. Another hypothesis stated that the Agent was a device buried in the moon by aliens during primordial times, set to detonate when certain conditions were met.\
    In any case, the result was that, first, the moon was fractured into seven large pieces, as well as innumerable smaller ones. And second, those pieces spread apart, enough to become observable as separate objects—huge rough boulders—but not enough to continue flying apart from one another. The moon’s pieces remained gravitationally bound, a cluster of giant rocks orbiting chaotically about their common center of gravity.\
    That point—formerly the center of the moon, but now an abstraction in space—continued to revolve around the Earth just as it had done for billions of years. So now, when the people of Earth looked up into the night sky at the place where they ought to have seen the moon, they saw instead this slowly tumbling constellation of white boulders. \
    Or at least that is what they saw when the dust cleared. For the first few hours, what had been the moon was just a somewhat-greater-than-moon-sized cloud, which reddened before the dawn and set in the west as the Utah astronomer looked on dumbfounded. Asia looked up all night at a moon-colored blur. Within, bright spots began to stand out as dust particles fell into the nearest heavy pieces. Europe and then America were treated to a clear view of the new state of affairs: seven giant rocks where the moon ought to have been."
    '''
    #short message
    #message = "Hellow world. Test stego code confirmed."
    #message = "Hello. I have successfully implemented steganography asap so get rollign. this can be fun"
    #message = "Hello world. I have implemented 3D steganography"
    
    #message = "Short story lets try this see how  far We can go how many values can we cave in this can this like have a long para without fucking up"
    
    #message = 
    #message = message.replace(".","")

    #message = message.replace("?","")
    
    message = "THE MOON BLEW UP WITHOUT WARNING AND FOR NO APPARENT reason. It was waxing, only one day short of full. The time was 05:03:12 UTC. Later it would be designated A+0.0.0, or simply Zero. An amateur astronomer in Utah was the first person on Earth to realize that something unusual was happening. Moments earlier, he had noticed a blur flourishing in the vicinity of the Reiner Gamma format is what we have to work with. apparently, we have to see how many more words it can take. It looks like a few more words might be added or maybe many more. The above example then was just a fucked up example with what going wrong, I have no idea. This looks cool, I can just keep on adding my entire stodr into this model. This tgree stegano"
    enc_data = stegano_encrypt(data,message)
    
    outF = open("myOutFile1.gcode", "w")
    print ("Message Encoded Successfully")
    for line in enc_data:
      # write line to output file
      outF.write(line)
      outF.write("\n")
    outF.close()
    
    

    

    

    

    


