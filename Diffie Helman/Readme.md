Diffie_Helman.py 

This script will calculate a Diffie Helamn shared key, and with that key, encrypt or decrypt a given message.

The input for this assignment will be 5 lines, and will take the form:

p
g
b
A
ciphertext/plaintext

This script assumes that you are Bob, and that the b above was chosen by you. A is Alice's public key. 
The ciphertext/plaintext will be in binary, and xor the given message with your calculated shared key in order to produce the decryption/encryption respectively. 
If the resulting binary string is plain english, indicate what the message says, otherwise return an indication that you have produced the ciphertext, and then output the binary string of the ciphertext.

Sample input: DHInput.txt



Diffie_Hellman_extra_credit.py

Use the same input as above, but this time instead of using binary xor on the provided text, you will use a method which differs depending on whether you are encrypting or decrypting, which means you will have to first determine whether your text is a plaintext or a ciphertext.

If the provided message is plaintext, encrypt by converting the binary plaintext into decimal and multiplying by the shared key (mod p). 
This generates a number that represents your ciphertext, so convert the number into binary and return that binary string.
If the provided message is a ciphertext, decrypt by converting it into decimal and multiplying by the inverse of the shared key mod p. 
With this number, convert to binary and finally output the plaintext.

