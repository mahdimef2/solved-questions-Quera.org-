input_string=input()
r,c =input_string.split()
r=int(r)
c=int(c)
if int(c) >=11 :
	print('Left',str(11-r),str(21-c))

else:
	print('Right',str(11-r),str(c))
	
