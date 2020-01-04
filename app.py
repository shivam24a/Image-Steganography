from PIL import Image
import encode
import decode

conti=1
while  conti:
	k=input("Press Key 1 : Encode \n          2 : Decode \n  Other key : Exit\n")
	if k=='1' :
		encode.Encode()
	elif k=='2' :
		decode.Decode()
	else :
		break
	conti=input("Want to Encode/Decode again(y/n) : ");
	if conti.upper()=='Y' or conti.upper()=='YES':
		conti=1
	else :
		conti=0
