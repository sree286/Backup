class Exception:
	list_a = [1,2,3,4,5]
	def __init__(self, ind):
		self.ind = ind
		self.upper_limit = len(self.list_a)
		self.lower_limit = -(self.upper_limit+1)
		if not str(ind).isnumeric():
			self.valueError()
		elif not (self.lower_limit <= int(self.ind) <= self.upper_limit):
			self.indexError()
		
	def indexError(self):
		print("The index {} is incorrect and index should lie between {} and {}".format(self.ind,self.lower_limit,self.upper_limit))

	def valueError(self):
		print("Use an Integer value as input")
		

Exception(int(input("Enter the index : ")))