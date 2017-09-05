import glob
import os
from Algs import *


class AlgFactory (object):
	"""This is the algFactory object.
	
	This creats and controls the instantiation of new objects
	
	It also provides the list of possible algoithms and helpdocs regarding 
		how to start each paticular algorithm
	
	Attributes:
	
		
	"""
	
	def __init__ (self):
		self.alg_list = []
		self.set_alg_list()
		None
		
	def get_alg_info(self, algName):
		"""
		Gets the docstring of a paticular algorithm
		"""
		
		algInfo = ""

		if algName not in self.alg_list:
			return "That algorithm selection does not seem to exist"
		
		algModule = globals()[algName]
		class_ = getattr(algModule, algName)
		algInfo = class_.__doc__ 
		return algInfo
		
	def set_alg_list(self):
	
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