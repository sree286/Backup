def pattern(rows):
	col = 5
	for row in range(rows):
	    count = col - row
	    if count<1: #prints underscore pattern after 5th row
	    	print((count+3)*" ",end = "")
	    	count = row - col + 2
	    	for c in range(count):
	    		print("_",end = " ")
	    	print()
	    else:       #prints star pattern
	    	print(row*" ",end='')
	    	for c in range(count):
	        	print("*",end = " ")
	    	print()

inp = int(input("Enter number :"))

if inp==1:
	pattern(5)

elif inp==2:
	pattern(9)

else:
	print("Invalid Input")
