from PIL import Image
codeword2='00011110'
bitlength=8
image=Image.new("1",(0,0))


def Decode():

	global image
	A_number_in_RGBA=3
	key=0
	tempstring=''
	checkpassword=''
	binary_decoded_list=[]
	element_counter=0
	address_to_decode=input("Enter Image Address to Decode : ")
	image=Image.open(address_to_decode)
	imagedata=(image.getdata())
	image.close()

	# image2=Image.new('1',(0,0))

	image2=Image.open(address_to_decode)
	image2=image2.resize((int(image.size[0]/2),int(image.size[1]/2)))
	image2.show()
	image2.close()

	codeword1=input("Enter Encode Password of the Image: ")+chr(int(codeword2,2))
	# image.close()

	for sublist in imagedata :
		for element_counter_in_sublist,element in enumerate(sublist):
			if element_counter_in_sublist==A_number_in_RGBA:
				continue
			else :
				tempstring+=(str(element%2))
			element_counter+=1
			if element_counter%bitlength==0:
				if key==0 :
					checkpassword+=chr(int(tempstring,2))
					if len(checkpassword)==len(codeword1):
						if tempstring==codeword2 and checkpassword==codeword1 :
							key=1
						else:
							key=2
							break
				elif key :
					if tempstring==codeword2:
						key=2
						break
					else :
						binary_decoded_list.append(tempstring);
						# tempstring=''
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
