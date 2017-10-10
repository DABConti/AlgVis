import glob
import os
from Algs import *


class AlgFactory (object):
	"""This is the algFactory object.
	
	This creats and controls the instantiation of new objects
	
	It also provides the list of possible algoithms and helpdocs regarding 
		how to start each paticular algorithm
		
	Input: visObj - Refrence to the Visualizer created by the controller
	
	Attributes:
	
		
	"""
	
	def __init__ (self, visObj):
		self.alg_list = []
		self.set_alg_list()
		self.visualizer = visObj
		None
		
	def get_alg_instance(self, algName):
		"""
		Get an instance of an Algorithm object that has been set up and is 
			ready to go
			
		Input: String Name of the algorithm class
		Output: Object
		
		"""
		
		if algName not in self.alg_list:
			print "That algorithm selection does not seem to exist"
			return "That algorithm selection does not seem to exist"
			
		#perform some jankyness to dynamicly get the class object (introspection)
		algModule = globals()[algName]
		class_ = getattr(algModule, algName)
		
		instance = class_()
		
		#get User input
		self.visualizer.handle_alg_input(instance)
		
		return instance
		
	def get_alg_info(self, algName):
		"""
		Gets the docstring of a paticular algorithm
		
		Input: String Name of the algorithm class
		Output: List
		"""
		
		algInfo = ""

		if algName not in self.alg_list:
			return "That algorithm selection does not seem to exist"
		
		#perform some jankyness to dynamicly get the class object
		algModule = globals()[algName]
		class_ = getattr(algModule, algName)
		algInfo = class_.__doc__ 
		
		return algInfo
		
	def set_alg_list(self):
		"""
		Sets the list of possible algorithms to run on class instantiation
		
		Input None
		Output: None
		"""
		
		dir_path = os.path.dirname(os.path.realpath(__file__))
		algorithms_path = dir_path + "/Algs"
		temp_list = []
		if (os.path.isdir(algorithms_path)):
			#check if path exists
			temp_list = glob.glob(algorithms_path + "/*.py")
		elif (os.path.isdir("/home/daniel/AlgVis")):
			#try the default install path
			temp_list = glob.glob("/home/daniel/AlgVis/*.py")
		else:
			raise Exception("Can not find algorithm directory, are you running this from " \
			"AlgVis folder?")
			
		for item in temp_list:
			if("__init__" not in item):
				self.alg_list.append(item.split("/")[-1].strip(".py"))
		
	def get_alg_list(self):
		"""
		Gets the list of possible algoithms
		
		Input None
		Output: List of possible files/classes 
				or an string saying that none can be found
		"""
			
		return self.alg_list