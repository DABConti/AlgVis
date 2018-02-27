from DefaultAlg import DefaultAlg

class MaximumSubarray(DefaultAlg):
	"""
	Maxium Subarray Algorithm
	
	Input: a list of n numbers
	Output: The 3 tuple containing the start and end index of the maximal subarray
		and the maximal sum
	"""
	
	

	def _defineName(self):
		"""
		Defines the name of this algorithm as presented to the end user
		
		This funtion should be re-implemented by each inheretors
		"""
		
		self.name = "Maximum-subarray"
		
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
		inputDef.append(["inputList", "The list of values to search for the maximal subarray", "listNumeric"])
		self.inputDef = inputDef
	
	def _defineDataStructs(self):
		"""
		Defines the objects that should be 'watched' for visualizition
		
		This funtion should be re-implemented by each inheretors
		"""
		dataStruts = {}
		dataStruts['workingSubArray'] = []
		dataStruts['outputSubArray'] = []
		
		self.dataStruts = dataStruts
		
	def run(self):
		"""
		Runs the maximal subarray problem
		"""
		
		listInput = self.inputs["inputList"]
		
		print listInput
		
		maxSubarray = self.findMaximumSubarray(listInput, 0, len(listInput) -1 )
		
		print maxSubarray
		
	
	def findMaximumSubarray(self, array, lowIndex, highIndex):
		"""
		Finds the maximumSubarry
		
		input:
			array - the array of values
			lowIndex - the start of the subarray that is examined by this function
			highIndex - the end of the subarray 
			
		return:
			int - the lowIndex of the maximalSubarray
			int - the highIndex of the maximalSubarray
			int - its sum
			
		"""
		
		if lowIndex == highIndex:
			#base case; only one element
			return lowIndex, highIndex, array[lowIndex]
		else:
			midIndex = (lowIndex + highIndex)/2
			
			leftLow, leftHigh, leftSum = self.findMaximumSubarray(array, lowIndex, midIndex)
			
			rightLow, rightHigh, rightSum = self.findMaximumSubarray(array, midIndex+1, highIndex)
			
			crossLow, crossHigh, crossSum = self.findMaxCrossingSubarray(array, lowIndex, midIndex, highIndex)
			
			if leftSum >= rightSum and leftSum >= crossSum:
				return leftLow, leftHigh, leftSum
			elif rightSum >= leftSum and rightSum >= crossSum:
				return rightLow, rightHigh, rightSum
			else:
				return crossLow, crossHigh, crossSum
			
		
	def findMaxCrossingSubarray(self, array, lowIndex, midIndex, highIndex):
		leftSum = None
		tempSum = 0
		
		i = midIndex
		
		while i >=lowIndex:
			tempSum += array[i]
			
			if tempSum > leftSum or leftSum is None:
				leftSum = tempSum
				maxLeft = i
			
			i-=1
		
		rightSum = None
		tempSum = 0
		i = midIndex + 1
		
		while i <= highIndex:
			tempSum += array[i]
			
			if tempSum > rightSum or rightSum is None:
				rightSum = tempSum
				maxRight = i
				
			i+=1
			
		return maxLeft, maxRight, leftSum+rightSum
		
		
		
