# Given number Find the column name

n = int(input())
#n = 104

name = ''
while n>0:
	rem = n%26

	if rem == 0:
		name += 'Z'
		n = (n // 26) - 1

	else:
		name += chr((rem - 1) + ord('A'))
		n = n//26

print(name[::-1])
