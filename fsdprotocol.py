class fsdprotocol(object):


	def __init__(self):
		self.__fsdaddpilot 		= 	"#AP"
		self.__fsdplaneinfo		=	"-PD"
		self.__fsdflightplan	=	"$FP"
		self.__fsdplaneparams	=	"-MD" #Legacy plane parameters
		self.__fsdpilotpos		=	"@"
		self.__fsdinforequest	=	"$CQ" #P2P request
		

	def FSDAddPilot(self):
		return "^"+self.__fsdaddpilot
	
	def FSDPlaneInfo(self):
		return "^\\"+self.__fsdplaneinfo
		
	def FSDFlightPlan(self):
		return "^\\"+self.__fsdflightplan
		
	def FSDPlaneParams(self):
		return "^"+self.__fsdplaneparams
		
	def FSDPilotPosition(self):
		return "^"+self.__fsdpilotpos

	def FSDInfoRequest(self):
		return self.__fsdinforequest