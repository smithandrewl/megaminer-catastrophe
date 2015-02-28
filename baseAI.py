# NOTE: this file should not be modified by competitors
idKey = "#"

# @class BaseAI: the basic AI functions that are the same between games
class BaseAI:
	def __init__(self, game, socket):
		self.socket = socket
		self.game = game

	def start(self, data):
		self.playerID = data["playerID"]
		self.init()


	# intended to be overridden by the AI class
	def init(self):
		pass


	#intended to be overridden by the AI class
	def run(self):
		pass


	#intended to be overridden by the AI class
	def ignoring(self):
		pass


	#intended to be overridden by the AI class
	def close(self):
		pass


	#intended to be called by the BaseGameAI class
	def sendCommand(self, command, *args):
		parameters = ""
		for arg in args:
			parameter = str(arg)
			if type(arg) is dict and arg["id"] > -1:
				parameter = idKey + str(arg["id"])
			
			command += parameter + " "
		parameters = parameters[:len(parameters)-1]
		
		self.socket.emit(command, parameters)