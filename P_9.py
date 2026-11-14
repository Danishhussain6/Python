# Q: Write a python program to encrypt and decrypt a message using ceaser cipher

# step 1:create key
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# step 2: create secret alphabet by shifting 3 positions
key = abc[3:]+abc[:3]
print(key)

# step 3:our secret message
msg="MEET AT CANTEEN"
# step 4: sender - create encryption mappimg
emap = str.maketrans(abc,key)

# step 5: Encrtpt the message
cipher_text=msg.translate(emap)

print("SENDER")
print("Original message:", msg)
print("Secret message :", cipher_text)

# step 6: Reciever - create decryption mapping
dmap=str.maketrans(key,abc)

# ````````````````````````````````````````````````````````````````````````````step 7: Decrypt the message
original_text=cipher_text.translate(dmap)

print("\nRECIEVER")
print("Recieved message:", cipher_text)
print("Decrypted message :", original_text)
