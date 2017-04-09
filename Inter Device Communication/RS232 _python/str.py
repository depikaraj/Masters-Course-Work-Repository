import bitarray
st=bitarray.bitarray()
st.extend('1000000000000001')
#st.extend('01010101011010010101001010101111')
print(len(st))
print(st)
k=0;

for i in range(0,len(st)//8):
	num=0
	for j in range (0,8):
		num+=st[i*8+j]*pow(2,j)
	n
	print (num)
		

