x=int(input())
n=int(input())

if n==0:
	print(20)
else:
	if n==7:
		print(x)
	if n>7 or n<=6 :
		if x-n < 0 :
			print(0)
		else:
			print(x-n)
