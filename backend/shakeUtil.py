import datetime
import math
from Shaker import *
from util import *

shakeActives = []

def addShaker(userId, gpsLoc, isRecruiter):
	try:
		x = 0
		while (x < len(shakeActives)):
			if(shakeActives[x].isToOld()):
				shakeActives.pop(x)
				x -= 1
			if(userId == shakeActives[x].userId):
				shakeActives[x] = Shaker(userId, gpsLoc, isRecruiter)
				return makeResponse("ADD_SHAKER", "SUCCESS", "User is already shaking, will remain active for 2 more mins", userId)
			x += 1
			
		shakeActives.append(Shaker(userId, gpsLoc, isRecruiter))
		return makeResponse("ADD_SHAKER", "SUCCESS", "User is now shaking, will remain active for 2 mins", userId)
	except e:
		return makeResponse("ADD_SHAKER", "FAILURE", str(e), userId)

def dist(x1, x2, y1, y2):
	print "in the dist"
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)
		
def getNearestShakers(userId, threshold):
	try:
		print "got in TRY"
		currentShaker = None
		results = []
		for elem in shakeActives:
			if elem.userId == userId:
				currentShaker = elem
				break
		if(currentShaker == None):
			return makeResponse("NEAREST_SHAKER", "FAILURE", "The passed userId is not curretly an active shaker", "")
		
		for elem in shakeActives:
			if(elem.userId != currentShaker.userId and not elem.isRecruiter and dist(elem.gpsLoc[0], currentShaker.gpsLoc[0], elem.gpsLoc[1], currentShaker.gpsLoc[1]) < threshold): 
				print "here"
				results.append(elem)
			print elem

		sortedResults = sorted(results, key=lambda x: dist(x.gpsLoc[0], currentShaker.gpsLoc[0], x.gpsLoc[1], currentShaker.gpsLoc[1]))
		print "sorted"

		sparseResults = []
		print sortedResults
		for elem in sortedResults:
			print "looping"
			sparseResults.append(elem.userId)
		return makeResponse("NEAREST_SHAKER", "SUCCESS", "Results Included", sparseResults)
	except e:
		return makeResponse("NEAREST_SHAKER", "FAILURE", str(e), "")
