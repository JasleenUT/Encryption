Steganography is the science of hiding the message in an image

Steps:
1. Convert the image to pixels
2. Find the length of the message
3. Convert the message into binary and pad it so that it is in bytes format
4. Append a semicolon at the end of the length
5. Append the message
The string to be encoded will be (length of the message + semicolon + message)
6. Replace the last 2 bits of every pixel by the string that has been created above
7. Convert the binary back to integer
8. Convert it into image


Decryption
1. Find the semicolon by picking up one byte at a time
2. The string before the semicolon is the length, so now we know how many bits we have to extract
3. Extract the message by extracting the last 2 bits from each pixel
4. You have the message

The image should be in png format
