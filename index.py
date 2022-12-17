def questionNumber(number):
    """Print the question number"""
    print("\n\n",f"{'-' * 30}Question {number}{'-' * 30}", "\n\n")
    
questionNumber("1.a")
print(*map(chr,[115,111,109,101,32,115,101,99,114,101,116,32,115,116,114,105,110,103]),sep="")

# I apply the chr function on the integer array that you give to convert the numbers to their corresponding ASCII characters



questionNumber("1.b")
hexString = hex(2438437403287867812943383341690399341847961660385418241405)
print(*map(chr,[int('0x%s%s'%(hexString[i],hexString[i+1]),base = 16) for i in range(2,len(hexString),2)]),sep="")
    
# FROM INTEGER TO HEXSTRING                    : First I convert the decimal value to hex string by using the hex function
# FROM HEXSTRING TO HEX BYTES                  : Then I convert the hex string in a list of hex bytes, by taking prefix "0x" and adding two character of the hex string (and looping on all the string except the two first character which are "0x")
# FROM HEXSTRING TO AN ARRAY OF ORDINAL VALUES : Next I convert the list of hex bytes in a list of int by writing "int(value,base = 16)" 
# FROM AN ARRAY OF ORDINAL VALUES TO RESULT    : Finally I get the hidden word by doing the same as question 1




questionNumber("2")
print(*map(chr,[ord(letter) ^ 13 for letter in "label"]),sep="")

# For each letter in the word label, convert this character in an integer value and then we apply the XOR which is reprensented by ^
# It gives us a value for each character, between 0 and 127, so we apply the chr method on each number we have, and we get the Unicode character for each value. We concatenated these values to get the final string output.





questionNumber("3")
def xor(hex1,hex2):
    """xor for two hex val"""
    return ''.join(format(int(a, 16) ^ int(b, 16),'x') for a,b in zip(hex1,hex2))
# I implement my own version of XOR using the built-in XOR operator ^

key1_2_3 = xor("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313","c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG = xor("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", key1_2_3)

print(*map(chr,[int('0x%s%s'%(FLAG[i],FLAG[i+1]),16) for i in range(0,len(FLAG),2)]),sep="")

# the final line is : FLAG ˆ KEY1 ˆ KEY3 ˆ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf so what I do above is :
# 1 - find the value of KEY1 ˆ KEY3 ˆ KEY2, which can be done easily by using my xor function with KEY1 and KEY2 ˆ KEY3 as input
# both KEY1 and KEY2 ˆ KEY3 hexadecimal values or given, so I can use my function and I get KEY1 ˆ KEY2 ˆ KEY3, which is exactly the same than KEY1 ˆ KEY3 ˆ KEY2 because of Commutative property
# 2 - I can then use the value 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf as input of my xor function with KEY1 ˆ KEY2 ˆ KEY3 and I get the flag.
# 3 - Finally I use almost the same line of code that I used in question 1.b to decode from hex to a readable string. 






questionNumber("4")
stringOrd = [elem for elem in bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")]

for order in range(256):
    possibleSecretMess = "".join(chr(o) for o in  [order ^ o for o in stringOrd])
    if possibleSecretMess.__contains__("crypto"):
        break
print("the secret message is : ",possibleSecretMess)

# First we convert the ciphertext (which is in hexadecimal) with the function bytes.fromhex() that converts it into a byte literal. We add each element in the list, so we have a list of values between 0 and 127
# Then I do a loop in the range(256) because our secret key is 1 byte long --> 8 bits --> 256 possible values
# For each possible keys, we xor the key value with each element of our list 'stringOrd' (created with the ciphertext)
# And then, on the same line, we use the chr function on the tab that we just created to get the Unicode character for each value
# The last function is used to give me only one output. I start by printing all the solutions that were possible with all the keys and search for one who makes sense. I find the one who start with crypto (like some previous exercise) so i decide to make a if statement and trigger a break to finish the loop when i find "possibLeSecretMess" which contains the word "crypto"












