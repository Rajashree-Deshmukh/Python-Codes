#Print out whole multiplication table of entered number.

num=int(input("Enter a number.."))

for i in range(1,11):
	print(num,'x',i,'=',num*i)
