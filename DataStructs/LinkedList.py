import Node

class LinkedList:
	
	def __init__(self, value = None):
		self.head = None
		self.size = 0
		
		if value != None:
			self.head = Node(value)
			size+=1
	
	def push(self, value):
		
		node = self.head
		
		if self.head == None:
			self.head = Node(value)
			size+=1
			return
		
		while True:
			if node.getNext() != None:
				node = node.getNext()
			else
				node.setNext(Node(value))
				size+=1
				return
				
	
		
		
	
