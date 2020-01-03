from PIL import Image
codeword2='00011110'
bitlength=8
total_numbers_in_mode=3;
image=Image.new('1',(0,0))

# imagedata=[[122,222,121],[143,154,145],[144,143,134],[134,144,155],[134,134,133],[154,176,154],[134,134,133],[122,122,121],[144,143,134],[134,144,155],[134,134,133],[122,122,121],[144,143,134],[144,143,134],[134,144,155],[134,134,133],[154,176,154],[134,134,133],[122,122,121],[144,143,134]]
def Encode():
	global image
	image_path=input("Enter Image Address to Encode : ")
	codeword1=input("Set Encode Password for the Image : ")
	image=Image.open(image_path)
	imagedata= list(image.getdata())
	# h,w=image.size()

	string_to_encode=input("Enter text to Encode : ")
	string_to_encode=codeword1+chr(int(codeword2,2))+string_to_encode
	binary_coversion_string=''
	for element in string_to_encode:
		binary_coversion_string+=format(ord(element),'08b')
	# s='111010011010'
	# print(s," !st")
	string_to_encode=binary_coversion_string + codeword2
	# print(string_to_encode," !st")
	while len(string_to_encode)%total_numbers_in_mode:
		string_to_encode+='0'
	element_counter=0
	imagedata_counter=0
	newlist=[]
	#encodetion
	for sublist in imagedata:
		for element in sublist:
			if element%2 !=int(string_to_encode[element_counter],2):
				element-=1;
			newlist.append(element)
			element_counter+=1;
		imagedata[imagedata_counter]=newlist
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
