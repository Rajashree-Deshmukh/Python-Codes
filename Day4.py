#thd=total hot dog
#thdpc=total hot dog per container
#tc=total container

thd=400
thdpc=8
tc=0
while(thd>=thdpc):
	thd=thd-thdpc
	tc+=1

print("Jack buy total",tc,"container")
