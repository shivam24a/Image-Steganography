from PIL import Image
codeword='10000000'
bitlength=8
total_numbers_in_mode=3;
image=Image.new("1",(0,0))
def Decode():
	address_to_decode=input("Enter image address to decode ")
	global image
	image=Image.open(address_to_decode)
	imagedata=(image.getdata())
	key=0
	tempstring=''
	binary_decoded_list=[]
	element_counter=0
	# print('now')
	for sublist in imagedata :
		for element in sublist:
			tempstring+=(str(element%2))
			element_counter+=1
			if element_counter%bitlength==0:
				# print(s,"this is k")
				if tempstring==codeword:
					tempstring=''
					key+=1;
					if key==2:
						break
				elif key==0:
					key=2
					break
				else :
					binary_decoded_list.append(tempstring);
					tempstring=''
		if key==2 :
			break
	decoded_string=''
	for element in binary_decoded_list:
		 decoded_string+=chr(int(element,2))
	print(decoded_string)