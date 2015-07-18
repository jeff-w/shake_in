import datetime
import math
from Shaker import *
from util import *

shakeActives = []

def addShaker(userId, gpsLoc, isRecruiter):
	try:
		x = 0
		while (x < len(shakeActives)):
			if(userId == shakeActives.userId):
				shakeActives[x] = Shaker(userId, gpsLoc, isRecruiter)
				return makeResponse("ADD_SHAKER", "SUCCESS", "User is already shaking, will remain active for 2 more mins", userId)
			if(shakeActives[x].isToOld()):
				shakeActives.pop(x)
				x -= 1
			x += 1
			
		shakeActives.append(Shaker(userId, gpsLoc, isRecruiter))
		return makeResponse("ADD_SHAKER", "SUCCESS", "User is now shaking, will remain active for 2 mins", userId)
	except e:
		return makeResponse("ADD_SHAKER", "FAILURE", str(e), userId)
		
		
def getNearestShakers(userId, threshold):
	try:
		currentShaker = None
		results = []
		for elem in shakeActives:
			if elem.userId == userId:
				currentShaker = elem
				break
		if(currentShaker == None):
			return makeResponse("NEAREST_SHAKER", "FAILURE", "The passed userId is not curretly an active shaker", "")
		for elem in shakeActives:
			if(elem.userId != currentShaker.userId and not elem.isRecruiter() and dist(elem.gpsLoc[0], currentShaker[0], elem.gpsLoc[1], currentShaker[1]) < threshold): 
				results.append(elem)
		sortedResults = sorted(results, key=lambda x: dist(x.gpsLoc[0], currentShaker[0], x.gpsLoc[1], currentShaker[1]))
		sparseResults = []
		for elem in sortedResults:
			sparseResults.append(elem.userId)
		return makeResponse("NEAREST_SHAKER", "SUCCESS", "User is currently shaking, will remain active for 2 mins", str(spareseResults))
	except e:
		return makeResponse("NEAREST_SHAKER", "FAILURE", str(e), "")


def dist(x1, x2, y1, y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)