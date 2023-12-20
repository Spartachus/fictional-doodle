alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
  b = []
  c = ""
  for i in text:
    b.append(alphabet.index(i)+shift)
  for i in b:
    c += alphabet[i]
  print(f"The encoded text is: {c}")
  
def decrypt(text,shift):
  b = ""
  c = ""
  for i in text:
    b=alphabet.index(i)
    d = b-shift
    c += alphabet[d]
  print(f"The decoded text is: {c}")
    
if direction == "encode":
  encrypt(text,shift)
elif direction == "decode":
  decrypt(text,shift)
#I used 2 different methods for the encryption i had an idea but couldn't execute lol
