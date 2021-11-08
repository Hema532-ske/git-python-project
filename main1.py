n=int(input())
p=n**(1/2)
for i in range(2):
	m=n/p
if(m==p):
	print("Perfect")
else:
	print("Not perfect")