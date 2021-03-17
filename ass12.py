str1=input("enter string :")
let,let1,dig,oth=0,0,0,0
for i in str1:
	if i.isupper():
		let+=1
	elif i.islower():
		let1+=1	

	elif i.isalnum():
		dig+=1
	else:
		oth+=1
print("Uppercae count=",let,"Lowercase count=",let1,"\ndigit count=",dig,"\nothers=",oth)

