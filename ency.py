import key
keygen = key.generated_key
message = "S"
letters = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
hex_dec = ''
encrypted_text = ''
L_Table = [['  ', '00', '19', '01', '32', '02', '1A', 'C6', '4B', 'C7', '1B', '68', '33', 'EE', 'DF', '03'],
            ['64', '04', 'E0', '0E', '34', '8D', '81', 'EF', '4C', '71', '08', 'C8', 'F8', '69', '1C', 'C1'],
            ['7D', 'C2', '1D', 'B5', 'F9', 'B9', '27', '6A', '4D', 'E4', 'A6', '72', '9A', 'C9', '09', '78'],
            ['65', '2F', '8A', '05', '21', '0F', 'E1', '24', '12', 'F0', '82', '45', '35', '93', 'DA', '8E'],
            ['96', '8F', 'DB', 'BD', '36', 'D0', 'CE', '94', '13', '5C', 'D2', 'F1', '40', '46', '83', '38'],
            ['66', 'DD', 'FD', '30', 'BF', '06', '8B', '62', 'B3', '25', 'E2', '98', '22', '88', '91', '10'],
            ['7E', '6E', '48', 'C3', 'A3', 'B6', '1E', '42', '3A', '6B', '28', '54', 'FA', '85', '3D', 'BA'],
            ['2B', '79', '0A', '15', '9B', '9F', '5E', 'CA', '4E', 'D4', 'AC', 'E5', 'F3', '73', 'A7', '57'],
            ['AF', '58', 'A8', '50', 'F4', 'EA', 'D6', '74', '4F', 'AE', 'E9', 'D5', 'E7', 'E6', 'AD', 'E8'],
            ['2C', 'D7', '75', '7A', 'EB', '16', '0B', 'F5', '59', 'CB', '5F', 'B0', '9C', 'A9', '51', 'A0'],
            ['7F', '0C', 'F6', '6F', '17', 'C4', '49', 'EC', 'D8', '43', '1F', '2D', 'A4', '76', '7B', 'B7'],
            ['CC', 'BB', '3E', '5A', 'FB', '60', 'B1', '86', '3B', '52', 'A1', '6C', 'AA', '55', '29', '9D'],
            ['97', 'B2', '87', '90', '61', 'BE', 'DC', 'FC', 'BC', '95', 'CF', 'CD', '37', '3F', '5B', 'D1'],
            ['53', '39', '84', '3C', '41', 'A2', '6D', '47', '14', '2A', '9E', '5D', '56', 'F2', 'D3', 'AB'],
            ['44', '11', '92', 'D9', '23', '20', '2E', '89', 'B4', '7C', 'B8', '26', '77', '99', 'E3', 'A5'],
            ['67', '4A', 'ED', 'DE', 'C5', '31', 'FE', '18', '0D', '63', '8C', '80', 'C0', 'F7', '70', '07']]

E_Table = [[ '01', '03', '05', '0F', '11', '33', '55', 'FF', '1A', '2E', '72', '96', 'A1', 'F8', '13', '35'],
            ['5F', 'E1', '38', '48', 'D8', '73', '95', 'A4', 'F7', '02', '06', '0A', '1E', '22', '66', 'AA'],
            ['E5', '34', '5C', 'E4', '37', '59', 'EB', '26', '6A', 'BE', 'D9', '70', '90', 'AB', 'E6', '31'],
            ['53', 'F5', '04', '0C', '14', '3C', '44', 'CC', '4F', 'D1', '68', 'B8', 'D3', '6E', 'B2', 'CD'],
            ['4C', 'D4', '67', 'A9', 'E0', '3B', '4D', 'D7', '62', 'A6', 'F1', '08', '18', '28', '78', '88'],
            ['83', '9E', 'B9', 'D0', '6B', 'BD', 'DC', '7F', '81', '98', 'B3', 'CE', '49', 'DB', '76', '9A'],
            ['B5', 'C4', '57', 'F9', '10', '30', '50', 'F0', '0B', '1D', '27', '69', 'BB', 'D6', '61', 'A3'],
            ['FE', '19', '2B', '7D', '87', '92', 'AD', 'EC', '2F', '71', '93', 'AE', 'E9', '20', '60', 'A0'],
            ['FB', '16', '3A', '4E', 'D2', '6D', 'B7', 'C2', '5D', 'E7', '32', '56', 'FA', '15', '3F', '41'],
            ['C3', '5E', 'E2', '3D', '47', 'C9', '40', 'C0', '5B', 'ED', '2C', '74', '9C', 'BF', 'DA', '75'],
            ['9F', 'BA', 'D5', '64', 'AC', 'EF', '2A', '7E', '82', '9D', 'BC', 'DF', '7A', '8E', '89', '80'],
            ['9B', 'B6', 'C1', '58', 'E8', '23', '65', 'AF', 'EA', '25', '6F', 'B1', 'C8', '43', 'C5', '54'],
            ['FC', '1F', '21', '63', 'A5', 'F4', '07', '09', '1B', '2D', '77', '99', 'B0', 'CB', '46', 'CA'],
            ['45', 'CF', '4A', 'DE', '79', '8B', '86', '91', 'A8', 'E3', '3E', '42', 'C6', '51', 'F3', '0E'],
            ['12', '36', '5A', 'EE', '29', '7B', '8D', '8C', '8F', '8A', '85', '94', 'A7', 'F2', '0D', '17'],
            ['39', '4B', 'DD', '7C', '84', '97', 'A2', 'FD', '1C', '24', '6C', 'B4', 'C7', '52', 'F6', '01']]
# Find co-primes of letter place holder
def find_prime_num(num,prime):

        for tprime in range(0,num + 1):
        # all prime numbers are greater than 1
                if tprime > 1:
                        for i in range(2, tprime):
                                if (tprime % i) == 0:
                                        break
                        else:
                              prime.append(tprime)  


# finding 2 primes of even placeholder
def two_prime_sum(num,prime):
    sum =0
    i=0
    j=0
    while i<len(prime):
        j=0
        while j<len(prime):
            sum = prime[i] + prime[j]
            if sum == num:
                sum_prime =[prime[i],prime[j]]
                return sum_prime
            j +=1
        i +=1

# finding 3 primes of odd placeholder
def three_prime_sum(num,prime):
    sum =0
    i=0
    j=0
    k=0
    while i<len(prime):
        j=0
        while j<len(prime):
            k=0
            while k<len(prime):
                sum = prime[i] + prime[j] + prime[k]
                if sum == num:
                    sum_prime =[prime[i],prime[j],prime[k]]
                    return sum_prime
                k +=1
            j +=1
        i +=1
# conversion of decimals into binary
def dec_to_bin(num):

    n = int(str(num), 10) 

    bint = ''
    while n > 0:
        bint = str(n % 2) + bint
        n = n >> 1  
    
    if len(bint) < 4:
        while len(bint) < 4:
            bint = str(0) + bint
    elif len(bint) < 8 and len(bint) > 4:
        while len(bint) < 8:
            bint = str(0) + bint
            
    return bint

# Adding bits segment when needed
def segment_add(bits):

    
    while len(bits) < 4:
        temp_bits = ''
        if len(bits) == 2:

            #xor 1st and 2nd segment to get 3rd segment
            y=int(bits[0],2) ^ int(bits[1],2)
            temp_bits = '{0:b}'.format(y)
            if len(temp_bits) < 4:
                while len(temp_bits) < 4:
                    temp_bits = str(0) + temp_bits
            bits.append(temp_bits)
        elif len(bits) == 3:

            i=0
            
            # take inverse of every 2nd bit from left till 4th segment has 4 bits
            while i < 2:
                j=1
                while j < 4:
                    y=int(bits[i][j],2) ^ int('1',2)
                    j += 2
                    temp_bits =  str(temp_bits) + str('{0:b}'.format(y))
                i +=1
            bits.append(temp_bits)
    


# xor between bits and key bits
def key_bits_xor(keygen,bits):
    after_bits = []
    i=0
    while i < 4:
        y=int(keygen[i],2) ^ int(bits[i],2)
        temp_bits = '{0:b}'.format(y)
        if len(temp_bits) < 4:
            while len(temp_bits) < 4:
                temp_bits = str(0) + temp_bits
        after_bits.append(temp_bits)
        i +=1
    return after_bits
    
# shifting of bits
def segment_bit_shifting(a):
    first_segment_state=False
    second_segment_state=False
    third_segment_state=False
    
    # if first segmnet have only 1 zero bit
    if int(a[0].count('0')) == 1:
        first_segment_state=True
    # if second segmnet have only 1 one bit   
    if int(a[1].count('1')) == 1:
        second_segment_state=True
    # if third and fourth segmnet combined have only 2 zero bits or 2 one bits
    if int(a[2].count('0') + a[3].count('0')) == 2:
            third_segment_state = True
    elif int(a[2].count('1') + a[3].count('1')) == 2:
            third_segment_state = True
    
    

    a = list(a[0] + a[1] + a[2] + a[3])

    # shift 1 bit to left side
    if first_segment_state == True:
        a.append(a[0])
        a.pop(0)
    # shift 2 bits to left side
    if second_segment_state == True:
        i = 0
        while i < 2:

            a.append(a[0])
            a.pop(0)
            i +=1
    # shift 4 bits to left side
    if third_segment_state == True:
        i = 0
        while i < 4:

            a.append(a[0])
            a.pop(0)
            i +=1
    
    temp_a = ''
    shifted_bits = []
    for i in a:
        temp_a = str(temp_a) + str(i)
        if len(temp_a) == 4:
            shifted_bits.append(temp_a)
            temp_a = ''

    return shifted_bits

# conversion of binary to hexadecimal
def bin_to_hex(b):
    i = 0
    temp_hex = []
    temp_hex_dec = ''
    while i < 4:
        temp_hex_dec += hex(int(b[i],2))[2:]
        
        if len(temp_hex_dec) == 2:
            temp_hex.append(temp_hex_dec)
            temp_hex_dec = ''

        i +=1
    return temp_hex


#converting from hexadecimal to decimal for L table plotting
def hex_to_dec(c):
    i=0
    temp_dec = []
    while i < 2:
        j=0
        while j < 2:
            temp_dec.append(int(str(c[i][j]), 16))
            j+=1
        i+=1
    return temp_dec

#Galois Field Multiplication using L and E table
def GLM(d,c,e):
    
    #finding value from L_table and adding it

    temp_l = hex(int(d[c[0]][c[1]],16)  + int(d[c[2]][c[3]],16))[2:]

    #if result exceeds FF, subtract from FF

    if len(temp_l) > 2: 
        temp_l = hex(int(temp_l,16) - int('FF',16))[2:]

    #finding value from E_table
    temp_l = e[int(temp_l[0],16)][int(temp_l[1],16)]
    
    return temp_l
# Start of message encryption

# if message letter is in lower case, then will convert to upper case first
if ord(message) > 90:
    message = chr(ord(message)-32)

# all letter placeholder will add upto 10 number first
letter_pos = letters.index(message)+10
prime = []


if letter_pos%2 == 0:
    # find co-prime of that number
    find_prime_num(letter_pos,prime)
    # find 2 primes which sum will result in message placeholder
    sum_prime = two_prime_sum(letter_pos,prime)   
elif letter_pos%2 != 0:
    # find co-prime of that number
    find_prime_num(letter_pos,prime)
    # find 3 primes which sum will result in message placeholder
    sum_prime = three_prime_sum(letter_pos,prime)

sum_prime = [13, 7, 9]
print("co-primes of message:",prime,"\naddition of prime numbers = message placeholder: ",sum_prime)
# conversion of those primes into binary
bits = []
i=0
while i < len(sum_prime):
    temp_bits = dec_to_bin(sum_prime[i])
    # if binary bits are 8, split it into 4/4 bits then append it into bits variable
    if len(temp_bits) > 4:
        bits.append(temp_bits[:4])
        bits.append(temp_bits[4:])
    # if binary bit is 4, append it into bits variable
    else:
        bits.append(temp_bits)
    i += 1

print("Binary bits: ",bits)

# if segment of bits does not match key segments, by rules will add segments
segment_add(bits)

print("Binary bits after segment: ",bits)

# xor with generated key and bits
key_xor_bits = key_bits_xor(keygen,bits)

print("Key: ",keygen)
print("bits after keygen xor: ",key_xor_bits)

# shifting bits by using 3 rules
shifted_bit = segment_bit_shifting(key_xor_bits)

print("bits after shifting: ",shifted_bit)

# conversion of binary bits into hexadecimal
hex_dec = bin_to_hex(shifted_bit)
print("Hexadecimal:", hex_dec)
dec_for_table_plot = hex_to_dec(hex_dec)

# using Galois Field Multiplication, getting encrypted text
encrypted_text = GLM(L_Table, dec_for_table_plot,E_Table)

print("Encrypted text:",encrypted_text)
