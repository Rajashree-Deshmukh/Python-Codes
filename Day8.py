
'''
On a certain day, the nurses at a hospital worked the following numberr of hours. Nurse Howard worked 8 hrs, Nurse Pease worked 10 hrs, Nurse Campbell worked 9 hrs, Nurse Grace worked 8 hrs, Nurse McCarthy worked 7 hrs and Nurse Murphy worked 12 hrs. What is the average number of hrs worked per nurse on this day?
Average should be as a float value.
'''


def avgWork(a,b,c,d,e,f,ncnt):
	totalHrs=float(a+b+c+d+e+f)
	#temp=float(totalHrs+ncnt)
	avgHrs=float(totalHrs/ncnt)

	return avgHrs


Howard=8
Pease=10
Campbell=9
Grace=8
McCarthy=7
Murphy=12
Nurse=6





avgHours=avgWork(Howard,Pease,Campbell,Grace,McCarthy,Murphy,Nurse)

print("Average Hours Worked is :",avgHours)
