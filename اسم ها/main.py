user_input=int(input())
a=[]
for i in range(user_input):
	word=input()
	a.append(word)
max_char=0
char=0
for i in a:
	list_char=[]
	for j in range(len(i)):
		if i[j] not in list_char:
			list_char+=i[j]
			char+=1
	if char >max_char :
		max_char=char
	char=0
print(max_char)
