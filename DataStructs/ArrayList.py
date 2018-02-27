class ArrayList:
	
	def __init__(self):
		self.array = []
		
	def get(self,index):
		return self.array[index]
		
	def insert(self, index, value):
		self.array.insert(index, value)
		return
