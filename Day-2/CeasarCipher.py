Title = '''

 #####                                         #####                                
#     #   ##   ######  ####    ##   #####     #     # # #####  #    # ###### #####  
#        #  #  #      #       #  #  #    #    #       # #    # #    # #      #    # 
#       #    # #####   ####  #    # #    #    #       # #    # ###### #####  #    # 
#       ###### #           # ###### #####     #       # #####  #    # #      #####  
#     # #    # #      #    # #    # #   #     #     # # #      #    # #      #   #  
 #####  #    # ######  ####  #    # #    #     #####  # #      #    # ###### #    # 

'''
print(Title)


def encode(text, shift):
    cipheredText = ""
    netshift=0
    for i in text:
        if ord(i)>=97 and ord(i)<=122:
            if (ord(i) + shift) > 122:
                netshift = (ord(i)+shift) - 122
                cipheredText += chr(96+netshift)
            else:
                cipheredText += chr(ord(i) + shift)
        else:
            cipheredText += i
    return cipheredText


def decode(text, shift):
    cipheredText = ""
    netshift = 0
    for i in text:
        if ord(i)>=97 and ord(i)<=122:
            if ord(i) - shift < 97:
                netshift = ord(i) - shift - 97
                cipheredText += chr(123+netshift)
            else:
                cipheredText += chr(ord(i)-shift)
        else:
            cipheredText += i
    return cipheredText


choice = input("Do you wanna start with the cipher(y/n): ")
while choice == 'y':
    cipherDirection = input("What do you wanna do(encode or decode): ")
    text = input("Enter the text you wanna cipher: ")
    shift = int(input("Enter the shift number: "))
    shift = shift%26
    if cipherDirection[0] == 'e':
        cipherText = encode(text, shift)
        print(f"The encoded text: {cipherText}")
    else:
        cipherText = decode(text, shift)
        print(f"The decoded text: {cipherText}")
    
    choice = input("DO you want to continue(y/n): ")

print("Thank you for using Caesar cipher!!")