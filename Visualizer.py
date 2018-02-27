import re
import sys
import urwid

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
				#remove non numeric, non -itive, and non comma characters
				
				non_decimal = re.compile(r'[^\d,-]+')
				
				parsedInput = non_decimal.sub('', enteredInput)
				parsedInput = parsedInput.replace(" ", "")
				parsedList = map(int, parsedInput.split(","))
				
				inputs[inputName] = parsedList
				
				
			else:
				raise StandardError("Invalid input type defined: ", str(inputType))
				
		algObj.setInput(inputs)
	
class VisDisplay:
	palette = [
		('body','default', 'default'),
		('foot','dark cyan', 'dark blue', 'bold'),
		('key','light cyan', 'dark blue', 'underline'),
		]
		
	footer_text = ('foot', ["Cmds:	", ('key', "b"), " (b)ack  ", ('key', "s"), " (s)tep  ", ('key', "t"), " step (t)en  ", ('key', "x"), " (e)xit  " ])
	
	def __init__(self, name):
		self.save_name = name
		self.walker = LineWalker(name)
		self.listbox = urwid.ListBox(self.walker)
		self.footer = urwid.AttrWrap(urwid.Text(self.footer_text),
			"foot")
		self.view = urwid.Frame(urwid.AttrWrap(self.listbox, 'body'),
			footer=self.footer)
		
	def main(self):
		self.loop = urwid.MainLoop(self.view, self.palette,
			unhandled_input=self.unhandled_keypress)
		self.loop.run()
	
	def unhandled_keypress(self, k):
		"""Last resort for keypresses."""
		
		if k == "b":
			None
		if k == "s":
			None
		if k == "t":
			None
		if k == "x":
			raise urwid.ExitMainLoop()
		else:
			return
		return True
			