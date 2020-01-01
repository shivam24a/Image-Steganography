from PIL import Image
import encode
import decode

k=int(input("Enter 1 for encode \n 2 for decode \n other key to exit\n"))
if k==1 :
	encode.Encode()
if k==2 :
	decode.Decode()