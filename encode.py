from PIL import Image
codeword2='00011110'
bitlength=8
total_numbers_in_mode=3
RGB_mode_number=3
image=Image.new('1',(0,0))

# imagedata=[[122,222,121],[143,154,145],[144,143,134],[134,144,155],[134,134,133],[154,176,154],[134,134,133],[122,122,121],[144,143,134],[134,144,155],[134,134,133],[122,122,121],[144,143,134],[144,143,134],[134,144,155],[134,134,133],[154,176,154],[134,134,133],[122,122,121],[144,143,134]]

def Encode():

	global image
	global total_numbers_in_mode
	image_path=input("Enter Image Address to Encode : ")
	image=Image.open(image_path)
	imagedata= list(image.getdata())
	image.close()

	image2=Image.open(image_path)
	image2=image2.resize((int(image.size[0]/2),int(image.size[1]/2)))
	image2.show()
	image2.close()
	total_numbers_in_mode=len(imagedata[0])
	# element_counter_in_sublist=0
	
	codeword1=input("Set Encode Password for the Image : ")
	string_to_encode=input("Enter text to Encode : ")
	string_to_encode=codeword1+chr(int(codeword2,2))+string_to_encode
	
	limit = int(((len(imagedata)*3)/8) - 2)
	if len(string_to_encode)*8>len(imagedata)*3:
		print("You can Enter at most",limit,"characters with Password in this Image")
		return 
	
	binary_coversion_string=''

	for element in string_to_encode:
		binary_coversion_string+=format(ord(element),'08b')
	string_to_encode=binary_coversion_string + codeword2

	while len(string_to_encode)%RGB_mode_number:
		string_to_encode+='0'
	element_counter=0
	imagedata_counter=0
	newlist=[]
	
	#encodetion
	# print(imagedata[:9])
	for sublist in imagedata:
		for element_counter_in_sublist in range(3):
			element=sublist[element_counter_in_sublist]
			if element%2 !=int(string_to_encode[element_counter],2):
				element=abs(element-1)
			newlist.append(element)			# newlist[element_counter_in_sublist]=element
			element_counter+=1;
		if total_numbers_in_mode==4:
			newlist.append(sublist[3])		# newlist[3]=sublist[3]
		imagedata[imagedata_counter]=newlist
		# print(newlist)
		newlist=[]
		imagedata_counter+=1
		if element_counter>=len(string_to_encode):
			break

	# print(imagedata)
	newimage=Image.new(image.mode,image.size)
	pixel_counter=0
	for y in range(image.size[1]):
		for x in range(image.size[0]):
			newimage.putpixel((x,y),tuple(imagedata[pixel_counter]))
			pixel_counter+=1
	
	encoded_save_address=input("Enter Address to save Image file : ")
	newimage.save(encoded_save_address)
	print("File saved")
