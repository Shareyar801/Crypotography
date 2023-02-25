key = [1, 2, 3, 6]
message = [1, 2, 2, 2]
S_Vector = [i for i in range(0, 8)]
Temp = [1, 2, 3, 6, 1, 2, 3, 6]
Cipher = []

print("\nPermutation of S-Vector:")
j = 0
for i in range(0, 8):
    j = (j + S_Vector[i] + Temp[i]) % 8
    S_Vector[i], S_Vector[j] = S_Vector[j], S_Vector[i]
    print("i: " + str(i) + ", S Vector: " + str(S_Vector))

i = 0
j = 0
o = 0
print("\nKey Generation: ")
for i in range(4):
    i = (i + 1) % 8
    j = (j + S_Vector[i]) % 8
    S_Vector[i], S_Vector[j] = S_Vector[j], S_Vector[i]
    t = (S_Vector[i] + S_Vector[j]) % 8
    key[o] = S_Vector[t]
    o += 1
    print("i: " + str(i)+", j: " + str(j)+ ", t: " + str(t) + ", Key: " + str(key))

print("\nEncryption: ")
for i in range(0, 4):
    a = str(bin(key[i]).replace("0b", ""))
    if(len(a) == 1):
        key_bi = "00" + a
    elif(len(a) == 2):
        key_bi = "0" + a
    elif(len(a) == 3):
        key_bi = a
    #print(key_bi)

    b = str(bin(message[i]).replace("0b", ""))
    if(len(b) == 1):
        mess_bi = "00" + b
    elif(len(b) == 2):
        mess_bi = "0" + b
    elif(len(b) == 3):
        mess_bi = b
    #print(mess_bi)

    cipher = str(int(key_bi) ^ int(mess_bi))
    if(len(cipher) == 2):
        cipher = "0" + cipher
    if(len(cipher) == 1):
        cipher = "00" + cipher
    
    print("key_bi: ", key_bi, ", mess_bi: ", mess_bi, ", cipher: ", cipher)
    Cipher.append(cipher)

print("\nEncrypted data in binary: ", Cipher)

