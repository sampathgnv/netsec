# Naga Guttikonda, 116699495

import sys

def caesar_str_enc(ciphertext,k):
	out = ""
	for char in ciphertext:
		out_char = caesar_ch_enc(char,k)
		out+=out_char
	return out		


def caesar_ch_enc(char,key):
	if(not char.isalpha()):
		return char
	elif (char.islower()):
		ascii_val = ord(char) - ord('a')
		encrypt = (ascii_val + key)%26
		encrypt+=ord('a')
		return chr(encrypt)
	elif (char.isupper()):
		ascii_val = ord(char) - ord('A')
		encrypt = (ascii_val + key)%26
		encrypt+=ord('A')
		return chr(encrypt)
	
def caesar_str_dec(ciphertext,k):
	out = ""
	for char in ciphertext:
		out_char = caesar_ch_dec(char,k)
		out+=out_char
	return out		


def caesar_ch_dec(char,key):
	if(not char.isalpha()):
		return char
	elif (char.islower()):
		ascii_val = ord(char) - ord('a')
		decrypt = (ascii_val - key)%26
		decrypt+=ord('a')
		return chr(decrypt)
	elif (char.isupper()):
		ascii_val = ord(char) - ord('A')
		decrypt = (ascii_val - key)%26
		decrypt+=ord('A')
		return chr(decrypt)


def driver_func():
	str_inp = sys.argv[2]
	inp = list(str_inp)
	key = int(sys.argv[1])
	
	enc = caesar_str_enc(inp,key)
	dec = caesar_str_dec(enc,key)
	
	print(enc)
	print(dec)

if __name__ == "__main__":
	driver_func()
