key = 6
message = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z." \
         " and a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y and z.\n"

def CeaserEncoder():
    encrypted_txt = '' 
    for i in range(len(message)):
        ascii_val = ord(message[i])
        if(ascii_val >= 65 and ascii_val <= 90):
            encrypted_txt += chr((ascii_val + key - 65) % 26 + 65)

        elif (ascii_val >= 97 and ascii_val <= 122):
            encrypted_txt += chr((ascii_val + key - 97) % 26 + 97)
        
        elif (ascii_val >= 32 and ascii_val <= 47):
            encrypted_txt += chr((ascii_val + key - 32) % 26 + 32)
    return encrypted_txt

def CeaserDecoder():
    decrypted_txt = '' 
    for i in range(len(encrypted_txt)):
        ascii_val = ord(encrypted_txt[i])
        if(ascii_val >= 65 and ascii_val <= 90):
            decrypted_txt += chr((ascii_val - key - 65) % 26 + 65)

        elif (ascii_val >= 97 and ascii_val <= 122):
            decrypted_txt += chr((ascii_val - key - 97) % 26 + 97)

        elif (ascii_val >= 32 and ascii_val <= 47):
            decrypted_txt += chr((ascii_val - key - 32) % 26 + 32)
    return decrypted_txt


print("Message: " + message)
encrypted_txt = CeaserEncoder()   
print("Cipher: " + encrypted_txt + "\n")
decryption_txt = CeaserDecoder() 
print("Decipher: " + decryption_txt + "\n")
