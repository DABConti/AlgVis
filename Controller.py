import cmd, sys, os
import Visualizer as Vis
import AlgFactory as AlgFact
import glob

class Controller (object):
	"""This is the controller for the Algorithm Visuialization module.

	It controls which alg is run, how it is run and the interface of the
	algorithm object and the final GUI
	
	Attributes:
	visualizer: the algorithm visualization object.
	algFactory: the algorithm factory ojects
	algInsance: an instance of a paticular algorithm (generated by 
		algFactory)
	controllerCLI: an instance of the command line intrepreter for the controller
	"""
	
	
	
	def __init__ (self, guiType = 'default'):
		"""
		Return an instance of the Controller for the AlgVis Module

		Params:
		guiType - eventually will determine if AlgVis will operate as a 
				stand alone command line system or as part of a larger system
				(ie my eventual website)
		"""
		self.visualizer = Vis.Visualizer(guiType)
		self.algFactory = AlgFact.AlgFactory(self.visualizer)
		
		if guiType == 'default':
			self.cmdLineController = CmdLineController()
			self.cmdLineController.setObjects(self.algFactory, self.visualizer)
			self.startCmdLine()
		else:
			#To be done 
			None
			
	def startCmdLine(self):
		"""
		Starts the controller command line intrepreter (CLI)
		"""
		self.cmdLineController.cmdloop()
	
	def start(self, algName = None, algInput = None):
		"""
		Starts a visualization of a paticular algorithm.
		"""
		#if algName == None:
		#	#Prompt the visualizer to ask for an alg name and alg input.
		#	#this.visualizer.
			
		None
		
class CmdLineController(cmd.Cmd):
	"""
	
	"""
	intro = "Welcome to the AlgVis shell"
	prompt = "(AlgVis)"
	file = None
	
	def setObjects(self, algFactory, visualizer):
		"""
		Initialies the refrences to the AlgFactory and visualizer objects.
		
		"""
		self.algFactory = algFactory
		self.visualizer = visualizer
	
	# --- ALGVis Shell commands ---
	"""
	ToDo:
	Run Alg
	Algorithms
	Get alg info
	
	"""
	def do_run(self, arg):
		"""
		Runs a paticular algorithm
		
		input: String of the algorithm to be run
		
		"""
		if( len(arg.split(" ")) > 1):
			print "\t Too many arguments." 
			print "\t Please input algorithm as a single word"
			print "\t IE. 'run DefaultAlg'"
		else:
			instance = self.algFactory.get_alg_instance(arg)
			
			#run algorithm, it will wait for the visualizer to tell it to go
			instance.run()
			
			
			#run visualizer
			
		
		
	def do_info(self, arg):
		"""
		Gets the info of a paticular algorithm
		
		input: String of the algorithm selected
		"""
		if( len(arg.split(" ")) > 1):
			print "\t Too many arguments." 
			print "\t Please input algorithm as a single word"
			print "\t IE. 'info DefaultAlg'"
		else:
			info = self.algFactory.get_alg_info(arg)
			print info
		
	def do_list(self, arg):
		"""
		Lists the possible algoithms
		"""
		files = self.algFactory.get_alg_list()
				
		for f in files:
			#print the files/classes
			print "    " + f
		
	
		
def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))
    
if __name__ == '__main__':
	controller = Controller()
	controller.startCmdLine()
	