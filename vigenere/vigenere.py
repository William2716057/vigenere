
#code to encrypt message
message = input("Enter message to be encoded: ")
plaintext = message.replace(" ", "")
plaintext = plaintext.lower()

#plaintext with spaces removed 
print("spaces removed: " + plaintext)
#keyword 
#key = "keyword" #add desired keyword here
key = input("Enter key to be used: ")

#keyword will be repeated until the length matches the plaintext 
key2 = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
print("key repeated to meet length of plaintext: " + key2)
#Convert texts to position numbers in the alphabet 
def char_positions(s):
    result = []
    for char in s:
        position = ord(char) - ord('a') 
        result.append(position)
    return result
input = plaintext

plainPos = char_positions(input)
print("position numbers of plaintext:")
print(plainPos)

keyPos = char_positions(key2)
print("position numbers of key:")
print(keyPos)
#Add index of each position in array to initial to get enciphered result 
#function must restart at 0 when reaching 26 (letter z)
def addResults(plainPos, keyPos):
    result = []

    for i in range(len(plainPos)):
        position_sum = (plainPos[i] + keyPos[i]) % 26

        result.append(position_sum)

    return result

enciphered = addResults(plainPos, keyPos)
print("position number of enciphered text:")
print(enciphered)

def backToLetters(final):
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    result = ''

    for position in final:
        if 0 <= position <= 26:
            letter = alphabet[position]
            result += letter
        else:
            result += '?'

    return result 

final = enciphered
letters = backToLetters(final)

print("result: " + letters)

print("Back to plaintext")
#code to decrypt message back to plaintext

#take encrypted message 
print("encryption: " + letters)
print(enciphered)
#keyword position numbers
print("keyword: " + key2)
print(keyPos)

#subtract keyword position numbers from encrypted message position numbers 
#(enciphered - keyPos)
def subtraction(encryptedPositions, keyPositions):
    result = []

    for i in range(len(encryptedPositions)):
        difference = (encryptedPositions[i] - keyPositions[i]) % 26

        result.append(difference)
    return result

decipheredPositions = subtraction(enciphered, keyPos)
print(decipheredPositions)

originalMessage = backToLetters(decipheredPositions)
print("Original Message: " + originalMessage)


