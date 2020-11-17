num1 =int(input('Enter First Num:-'))
num2 =int(input('Enter Second Num:-'))
num3 =int(input('Enter Third Num:-'))
if (num1>=num2) and (num1>=num3):
	largest=num1
elif (num2>=num1) and (num2>=num3):
	largest=num2
else:
	largest=num3

print('Largest num among three is:-',largest)
