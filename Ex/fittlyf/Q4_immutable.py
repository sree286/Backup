t1 = (1,2,3,4)
print("Immutability means Once it created we cannot modify elements in it. It means we cannot perform actions such as adding, deleting.")
try:
	t1[2] = 5
except Exception as e:
	print("Tuple is immutable because we cannot add/delete elements in the tuple, below is the error we get because we are trying to change the element in index 2. But tuple is immutable and we cannot modify it.")
	raise e