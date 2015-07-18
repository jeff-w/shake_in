import datetime

class Shaker:
	def __init__(self, userId, gpsLoc, isRecruiter):
		self.userId = userId
		self.gpsLoc = gpsLoc
		self.startTime = datetime.datetime.now()
		self.isRecruiter = isRecruiter
		
	def isToOld(self):
		return (datetime.datetime.now() - self.startTime).total_seconds() > 120 #two mins
		
	def isRecruiter(self):
		return self.isRecruiter