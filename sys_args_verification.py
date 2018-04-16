import sys

z=int(len(sys.argv))

if z < 3 or z > 3 :
	print ("***Invalid no of arguements***")
	print ("***Pass only 2 arguements***")
	sys.exit(0)

x=int(sys.argv[1])
y=int(sys.argv[2])

if x <= 0  or  y <= 0 :
	print("***Improper arguements***")
	print("***Numbers should be positive integers***")
	sys.exit(0)

if x > y :
	q = x / y
	print(int(q)) 
else :
	q = y / x
	print(int(q))

