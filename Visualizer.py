import re

class Visualizer (object):
	"""This is the Visualizer.
	
	Attributes:
	guiType: the type of the GUI to make:
		
	"""
	
	def __init__ (self, guiType):
		self.guiType = guiType
		
	def handle_alg_input(self, algObj):
		"""
		Takes a paticular algorithm object and querries the user for the 
			correct input and sets it.
		"""
		
		inputDef = algObj.getInputDef()
		inputs = {}
		
		print "Please enter the following inputs for the ", algObj.getName(), " algorithm:"
		
		for item in inputDef:
			inputName = item[0]
			inputDes  = item[1]
			inputType = item[2]
			
			if inputType == "listNumeric":
				inputDes += ", please enter a comma seperated list of numbers" 
			else:
				#unhandled functionality todo throw error
				None
			
			print "\t", inputDes, ":"
			
			enteredInput = raw_input()
			#todo handle escape character
			
			#parse and safely handle input according to its types
			if inputType == "listNumeric":
				#remove non numeric and non comma characters
				
				non_decimal = re.compile(r'[^\d,]+')
				
				parsedInput = non_decimal.sub('', enteredInput)
				parsedInput = parsedInput.replace(" ", "")
				parsedList = map(int, parsedInput.split(","))
				
				inputs[inputName] = parsedList
				
				
			else:
				raise StandardError("Invalid input type defined: ", str(inputType))
				
		algObj.setInput(inputs)