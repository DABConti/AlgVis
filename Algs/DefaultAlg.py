
class DefaultAlg (object):
	"""
	Superclass for the possible algorithms
	
	List Reversal Algorithm
	Input: A list of n numbers (input)
	Output: That list in reversed order
	Complexity:
	"""
	
	def __init__ (self):
		"""
		Returns an instance of the Default Alg Class
		"""
		#set its name
		self._defineName()
		
		#the definitions of the inputs
		self.inputDef = []
		self._defineInput()
		
		#the inputs themselves
		self.inputs = {}
		
		#the dictionary of the data structures that are relivent to visualization
		self.dataStruts = {}
		self._defineDataStructs
	
	def _defineName(self):
		"""
		Defines the name of this algorithm as presented to the end user
		
		This funtion should be re-implemented by each inheretors
		"""
		
		self.name = "List Reversal"
		
		
	def _defineInput(self):
		"""
		Defines the required input of the algorithm
		
		This funtion should be re-implemented by each inheretors
		"""
		# inputs should be defined as an individual entry in the inputDef
		# A defininition of one input would look like
		# inputdef = [["inputList", "The list of numbers to be reversed", "list"]]
		# 			Name of the input, a descriptor of the input, 
		#  			a definition of how the user should be input the data
		inputDef = []
		inputDef.append(["inputList", "The list of numbers to be reversed", "listNumeric"])
		self.inputDef = inputDef
		
	def getInputDef(self):
		return self.inputDef
		
	def getName(self):
		return self.name
		
	def _defineDataStructs(self):
		"""
		Defines the objects that should be 'watched' for visualizition
		
		This funtion should be re-implemented by each inheretors
		"""
		dataStruts = {}
		dataStruts['outputList'] = []
		self.dataStruts = dataStruts
		
	def setInput(self, inputs):
		"""
		Sets the required input for this algorithm
		
		Params:
		inputs - A dictionary of inputs. The keys should match the defined input
		"""
		#check if inputs is valid
		
		reqInputNames = [i[0] for i in self.inputDef]
		
		if len(reqInputNames) != len(inputs) or not (set(reqInputNames) & set(inputs.keys())):
			# an error has occured
			raise StandardError("Invalid number/names of inputs for algorithm,"
				                 " expected: ", str(reqInputNames), \
				                 " recieved: ", str(inputs.keys()))
		
		for inDef in self.inputDef :
			inputName = inDef[0]
			self.inputs[inputName] = inputs[inputName]
		
			
	
	def getAlgDocs(self):
		"""
				
		"""
		
		return self.__doc__

