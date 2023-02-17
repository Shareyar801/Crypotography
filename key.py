# importing libraries
import math as m
from math import floor
import binascii as bina
from binascii import hexlify
import binary as bin
# calculating elements collatz conjecture

def modular_calculate(x):
    if x == 0 or x == 1:
        return int(0)
    elif x%2 == 0:
        return int(x / 2)
    elif x%2 == 1:
        return (3 * x +1)
# pops first element
def first_element_pop():
    f0.pop(0)
    f1.pop(0)
    f2.pop(0)
    f3.pop(0)
    f4.pop(0)
    f5.pop(0)
    f6.pop(0)
    f7.pop(0)

# hexa to binary conversion
def hexa_to_binary(x):
    letter = x.encode()
 
    a = (hexlify(letter).decode())
    
    n = int(a, 16) 
    
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1  
    
    while len(bStr) < 8:
        bStr = str(0) + bStr
        res = bStr
        
    return res

# calculating Xn using linear congruential method
def LC(x):  
    j=0
    X= [x]
    while j < 7:
    
        X.append((a * X[j] + c) % m)
        j +=1

    return X


#S-BOX plotting (Key size must be 13 letters)

def s_box_plot():
    i =0
    j=0
    w=-1
    c=8
    s_box = []
    temp_box=[]
    while j < 10: 
        i = 0  
        while i < 10:
            if c == 8:
                w = w + 1
                temp = hexa_to_binary(word[w])

                c=0
            temp_box.append(temp[c])
            if len(temp_box) == 10:
                s_box.append(temp_box)
                temp_box=[]
            i = i+1
            c = c+1
        j = j+1
    return s_box
#s_box -> keygen plotting
def key_gen_plot(sbox,btl,m):
    i=0
    key_gen = []
    temp_key = ''
    while i <btl:
        temp_mod = str(m[i])
        if int(temp_mod) > 10:
            temp_key =  temp_key+sbox[int(temp_mod[0])][int(temp_mod[1])]
        else:
            temp_key =  temp_key+(sbox[0][int(temp_mod[0])])
        temp_key
        if len(temp_key) == 4:
            key_gen.append(temp_key)
            temp_key = ''
        i = i+1
    return key_gen
#initializing values

a = 11
m = 17
c = 14
x0 = 9
word = "Assignment 02"
print("a:",a,", c:",c,", x0:",x0,",m:",m,"keyword:",word)

# finding Xn using linear congruential method
Xn = LC(x0)

print("Xn =", Xn)

# initializing each Xn for collatz conjecture 
f0 = [Xn[0]]
f1 = [Xn[1]]
f2 = [Xn[2]]
f3 = [Xn[3]]
f4 = [Xn[4]]
f5 = [Xn[5]]
f6 = [Xn[6]]
f7 = [Xn[7]]

i=0
j=0

# calculating each element collatz conjecture value till it reaches 1 or 0
while (f0[i] != 1 and f0[i] != 0) or (f1[i] != 1 and f1[i] != 0) or (f2[i] != 1 and f2[i] != 0) or (f3[i] != 1 and f3[i] != 0) or (f4[i] != 1 and f4[i] != 0) or (f5[i] != 1 and f5[i] != 0) or (f6[i] != 1 and f6[i] != 0) or (f7[i] != 1 and f7[i] != 0):
    f0.append(modular_calculate(f0[i]))
    f1.append(modular_calculate(f1[i]))
    f2.append(modular_calculate(f2[i]))
    f3.append(modular_calculate(f3[i]))
    f4.append(modular_calculate(f4[i]))
    f5.append(modular_calculate(f5[i]))
    f6.append(modular_calculate(f6[i]))
    f7.append(modular_calculate(f7[i]))

    i +=1
first_element_pop()
print("",Xn[0] ,"=",f0,"\n",Xn[1] , "=",f1,"\n",Xn[2] , "=",f2,"\n",Xn[3] , "=",f3,"\n",Xn[4] , "=",f4,"\n",Xn[5] , "=",f5,"\n",Xn[6] , "=",f6,"\n",Xn[7] , "=",f7)

# addition of Fn elements then applying mod 100
mod = []
while j < i:
    Sum = f0[j]+f1[j]+f2[j]+f3[j]+f4[j]+f5[j]+f6[j]+f7[j]
    mod.append(Sum % 100)
    j +=1

print("F = ",mod)

# using bits according to the length of F nearest lower bit
bits = [2,4,8,16,32,64,128,256,512]
modlen = len(mod)

i = len(bits)
j=0
while j < i-1:
    if modlen >= int(bits[j]) and modlen < bits[j+1]:
        bits_len = bits[j]
    j +=1
print("Total Bits being used for key-gen:",bits_len)

# using keyword, generating binary S-box
S_box = s_box_plot()

print("\t  *********BINARY S-BOX*********")
for i in S_box:
    print(i)

# will generate key from S-box matrix
generated_key = key_gen_plot(S_box,bits_len,mod)

print("Generated key:", generated_key )