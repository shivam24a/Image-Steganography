from PIL import Image
codeword2='00011110'
bitlength=8
total_numbers_in_mode=3;
image=Image.new("1",(0,0))
def Decode():
	address_to_decode=input("Enter Image Address to Decode : ")
	codeword1=input("Enter Encode Password of the Image: ")+chr(int(codeword2,2))
	global image
	image=Image.open(address_to_decode)
	imagedata=(image.getdata())
	key=0
	tempstring=''
	checkpassword=''
	binary_decoded_list=[]
	element_counter=0
	# print('now')
	for sublist in imagedata :
		for element in sublist:
			tempstring+=(str(element%2))
			element_counter+=1
			if element_counter%bitlength==0:
				# print(s,"this is k")
				# tempstring+=tempb
				if key==0 :
					checkpassword+=chr(int(tempstring,2))
					if len(checkpassword)==len(codeword1):
						if tempstring==codeword2 and checkpassword==codeword1 :
							# tempstring=''
							key=1
						else:
							# tempstring=''
							key=2
							break
				elif key :
					if tempstring==codeword2:
						key=2
						break
					else :
						binary_decoded_list.append(tempstring);
						tempstring=''
				tempstring=''
		if key==2 :
			break
	decoded_string=''
	for element in binary_decoded_list:
		 decoded_string+=chr(int(element,2))
	# print(checkpassword) 
	if len(decoded_string)==0:
		print("Either you Entered wrong Password or Image has no text hidden")
	else :
		print("Hidden text : ",decoded_string)
