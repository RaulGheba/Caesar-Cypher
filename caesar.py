alphabet = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input(f"Type your message. \n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(text,shift):

 encryptedWord=""
 
 for letter in text:
  position=alphabet.index(letter)   
     
  encryptedWord+=alphabet[position+shift]
 print(f"Encrypted word: {encryptedWord}")                                        

def decrypt(text,shift):
    
 decryptedWord=""
 for letter in text:
     position=alphabet.index(letter)-shift   
     decryptedWord+=alphabet[position]
 print(f"Decrypted word: {decryptedWord}")


if direction=="encode":
    encrypt(text,shift)
if direction=="decode":
    decrypt(text,shift)
if direction!="encode" and direction!="decode":
    print("Incorrect input!")