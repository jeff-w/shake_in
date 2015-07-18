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
	

def addUser(user_db, recruiter_db, firstName, lastName, password, emailAddress, phoneNumber, school, eduLevel, GPA, skills):
	dbResponse = queryToList(user_db.find({ 'userName' : emailAddress }))  # Query the database for the provide username
	if len(dbResponse) >= 1:                                               # We received multiple responses - this should not be possible
		return makeResponse("CREATE_USER", "FAILURE", "That email address is already being used by another user", "")
	dbResponse = queryToList(recruiter_db.find({ 'userName' : emailAddress }))
	if len(dbResponse) >= 1:                                               # We received multiple responses - this should not be possible
		return makeResponse("CREATE_USER", "FAILURE", "That email address is already being used by another recruiter", "")
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
	return makeResponse("CREATE_USER", "SUCCESS", "User account was created successfully", str(id))
	           
def addRecruiter(user_db, recruiter_db, firstName, lastName, password, emailAddress, phoneNumber, school, eduLevel, GPA, skills):
	dbResponse = queryToList(user_db.find({ 'userName' : emailAddress }))  # Query the database for the provide username
	if len(dbResponse) >= 1:                                               # We received multiple responses - this should not be possible
		return makeResponse("CREATE_USER", "FAILURE", "That email address is already being used by another user", "")
	dbResponse = queryToList(recruiter_db.find({ 'userName' : emailAddress }))
	if len(dbResponse) >= 1:                                               # We received multiple responses - this should not be possible
		return makeResponse("CREATE_USER", "FAILURE", "That email address is already being used by another recruiter", "")
	id = db.insert_one({'userName':emailAddress, 
	           'firstName':firstName, 
	           'lastName':lastName, 
	           'password':password, 
	           'emailAddress':emailAddress, 
	           'phoneNumber':phoneNumber, 
	           'company':school}).inserted_id
	return makeResponse("CREATE_RECRUITER", "SUCCESS", "User account was created successfully", str(id))
	
	
	
def validateLogin(user_db, recruiter_db, userName, password):
	dbResponse = queryToList(user_db.find({ 'userName' : userName, 'password' : password }))
	if len(dbResponse) == 1:                                               # If we found a match of the person's log in info, then we are all good and they can log in
		return makeResponse("LOGIN", "SUCCESS", "USER", str(dbResponse[0]['_id']))
	dbResponse = queryToList(recruiter_db.find({ 'userName' : userName, 'password' : password }))
	if len(dbResponse) == 1:                                               # We received multiple responses - this should not be possible
		return makeResponse("LOGIN", "SUCCESS", "RECRUITER", str(dbResponse[0]['_id']))
	return makeResponse("LOGIN", "FAILURE", "Password and username do not match database, invalid login", "")
	