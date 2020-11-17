f=int(input("Enter free bytes :"))
u=int(input("Enter used bytes :"))
o=int(input("Enter old file size :"))
n=int(input("Enter new file size :"))

totaldisksize=f+u
currentusedsize=u+o
currentusedsize=currentusedsize+n
currentfreesize=totaldisksize-currentusedsize

print("Free Space Available",currentfreesize,"bytes")
