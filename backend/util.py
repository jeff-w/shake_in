# Converts a cursor object (returned from MongoDB request)
# into a list by iterating over it (not super efficient)
def queryToList(cursorObject):
	myList = []
	for document in cursorObject:
		myList.append(document)
	return myList
	
def makeResponse(action, result, desc, userID):
	responseDict = { 'action' : action, 'result' : result, 'desc' : desc, 'userID' : userID }
	print "response made"
	print responseDict
	return responseDict
	

def addUser(db, firstName, lastName, password, emailAddress, phoneNumber, school, eduLevel, GPA, skills):
	dbResponse = queryToList(db.find({ 'userName' : emailAddress }))  # Query the database for the provide username/password combo
	if len(dbResponse) >= 1:                                          # We received multiple responses - this should not be possible
		return makeResponse("CREATE_USER", "FAILURE", "That email address is already being used", "")
	id = db.insert_one({'userName':emailAddress, 
	           'firstName':firstName, 
	           'lastName':lastName, 
	           'password':password, 
	           'emailAddress':emailAddress, 
	           'phoneNumber':phoneNumber, 
	           'school':school, 
	           'eduLevel':eduLevel, 
	           'GPA':GPA, 
	           'skills':skills}).inserted_id
	makeResponse("CREATE_USER", "SUCCESS", "User account was created successfully", str(id))
	           
def addRecruiter(db, firstName, lastName, password, emailAddress, phoneNumber, school, eduLevel, GPA, skills):
	dbResponse = queryToList(db.find({ 'userName' : emailAddress }))  # Query the database for the provide username/password combo
	if len(dbResponse) >= 1:                                          # We received multiple responses - this should not be possible
		return makeResponse("CREATE_RECRUITER", "FAILURE", "That email address is already being used", "")
	id = db.insert_one({'userName':emailAddress, 
	           'firstName':firstName, 
	           'lastName':lastName, 
	           'password':password, 
	           'emailAddress':emailAddress, 
	           'phoneNumber':phoneNumber, 
	           'company':school}).inserted_id
	makeResponse("CREATE_RECRUITER", "SUCCESS", "User account was created successfully", str(id))