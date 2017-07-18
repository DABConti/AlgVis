import cmd, sys
import Visualizer as Vis
import AlgFactory as AlgFact

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
		self.algFactory = AlgFact.AlgFactory()
		self.algInstance = None
		self.cmdLineController = CmdLineController()
		
		if guiType == 'default':
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
	
	
	# --- ALGVis Shell commands ---
		
def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))
    
if __name__ == '__main__':
	controller = Controller()
	