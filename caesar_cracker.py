'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''
import string
abc_list = list(string.ascii_lowercase)
last_index_abc = len(abc_list) - 1

def decrypt_message(message, key):
  encrypted_message = ""
  for letter in message:
    encrypted_letter = ""
    
    try:
      abc_list_index = abc_list.index(letter.lower())
      if abc_list_index - key < 0:
        desc_position = abc_list_index - key
        encrypted_letter = abc_list[desc_position]
      else: 
        encrypted_letter = abc_list[abc_list_index - key]
    except ValueError as e:
      encrypted_letter = letter  

    encrypted_message += encrypted_letter
  return encrypted_message



encrypted_message = "qiix qi fc xli vswi fywliw xsrmklx."

print("============== Possible Messages ==============:\n")
for key in range(0, last_index_abc + 1):
  print(f"Key: {key} | Message: {decrypt_message(encrypted_message, key)}")




